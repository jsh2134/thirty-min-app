import time
import os

from fabric.api import env
from fabric.api import sudo, run, put
from fabric.exceptions import NetworkError

import ec2
import settings

env.key_filename = settings.SECRETS['aws_key_pair']

def create_instance():
	""" Just Creates an Instance """
	instance = ec2.create_new_instance()


def deploy_web():

	# Create New Instance
	instance = ec2.create_new_instance()

	# Set Env Host String
	env.host_string = "ec2-user@%s" % (instance.ip_address) 
	
	# Install Web
	connect_attempts = 0
	while connect_attempts <= 3:
		try:
			install_web()
			break
		except NetworkError:
			print "Failed to connect: used attempt %s of 3" % \
											(connect_attempts)
			connect_attempts += 1
			time.sleep(10)
		except:
			print "Failed to install_web"
			break

	return True


def install_web():

	remote_dir = '/home/ec2-user/'
	remote_code_dir = os.path.join(remote_dir, 'code')

	# Install packages with yum
	sudo('yum install -y git gcc nginx')

	# Install pip
	sudo('curl -O http://pypi.python.org/packages/source/p/pip/pip-1.0.tar.gz')
	run('tar xvfz pip-1.0.tar.gz')
	sudo('cd pip-1.0 && python setup.py install')
	
	# start nginx
	put('nginx.conf', '/etc/nginx/', use_sudo=True)
	sudo('service nginx start')

	# Install python requirements
	put('requirements.txt', remote_dir)
	sudo('pip install -r %s/requirements.txt' % (remote_dir))
	
	# Checkout Code from GitHub
	github_fingerprint = "github.com,207.97.227.239 ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ=="

	sudo(""" echo '%s' >> .ssh/known_hosts """ % github_fingerprint , pty=True)
	put("ssh-config", ".ssh/config", mode=0600)
	put('keys/deploy_key.pub', '.ssh/')
	put('keys/deploy_key', '.ssh/', mode=0600)
	sudo('git clone %s %s' % (settings.REPO_URL, remote_code_dir) )

	# Start Application
	sudo('python %s/app.py > /var/log/app_log.log &' % (remote_code_dir) )



# Test Functions
################
def host_type():
	run('uname -a')

def free_space():
	run('df -h')

def what_is_my_name():
	run('whoami')

def what_is_sudos_name():
	sudo('whoami')


