Thirty Minute Python Web App on Amazon
============================================

Build and Deploy a Python Web App to Amazon in 30 minutes


Setup
================================

Install Fabric, Flask and Boto
---------------------------------

::

	 $ pip install fabric flask boto


Create an Amazon Web Services Account
-----------------------------------------

- Go to `Amazon Web Services <http://aws.amazon.com/>`_ and Sign Up for an account.
- Currently there is `a Free Tier <http://aws.amazon.com/free/>`_ for new customers for some instance sizes
- Create a `Default Key Pair <http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/generating-a-keypair.html#how-to-have-aws-create-the-key-pair-for-you>`_


Create a Local Settings File that Stores Amazon settings
----------------------------------------------------------
::

        # Sample local_settings.py

        # Amazon Values
        aws_key = 'DFGTAKIAJ4HFA'
	aws_secret = 'ASklKUYljkja97Kjk+adsasd/adsdssdsds'
	aws_key_path = '/home/foobar/.ssh/aws_keypair.pem'
	aws_key_pair = 'my_keypair_name'
	aws_security_group = 'default'

        # Github Value
	github_user = 'my_github_name'


Deploy the Code to Amazon Server
----------------------------------

NOTE: Whenever you deploy instances to Amazon you will be charged the hourly rate per instance type. The below command will start the clock on charges until you Stop or Terminate an instance.

::

        $ fab deploy_web

Customize
-------------

Edit variables defined in settings.py AWS global variable to change `Amazon instance size <http://aws.amazon.com/ec2/instance-types/>`_ and `Machine Images <https://aws.amazon.com/amis>`_


::

        'defaults' : {
                'image_id' : 'ami-aecd60c7',       # Amazon Linux 64-bit
                'instance_type' : 't1.micro',      # Micro Instance


