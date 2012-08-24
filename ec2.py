from boto.ec2.connection import EC2Connection
from settings import SECRETS

import time

SERVER = {
		'image_id' : 'ami-aecd60c7',
		'instance_type' : 't1.micro',
		'security_groups' : SECRETS['aws_security_groups'],
		'key_name' : SECRETS['aws_key_pair'],
}


class EC2Conn:

	def __init__(self):
		self.conn = None


	def connect(self):
		self.conn = EC2Connection(SECRETS['aws_key'],
								  SECRETS['aws_secret'])

	def create_instance(self):
		reservation = self.conn.run_instances( **SERVER)
		print reservation
		instance = reservation.instances[0]
		time.sleep(10)
		while instance.state != 'running':
			time.sleep(5)
			instance.update()
			print "Instance state: %s" % (instance.state)
		
		# Sleep for a bit more before trying to connect
		time.sleep(60)

		print "instance %s done!" % (instance.id)

		return instance


def create_new_instance():
	a = EC2Conn()
	a.connect()
	return a.create_instance()

