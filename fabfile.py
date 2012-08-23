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
	put('keys/deploy_key.pub', '.ssh/')
	put('keys/deploy_key', '.ssh/id_rsa', mode=0600)
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


