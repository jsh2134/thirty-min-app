Thirty Minute Python Web App
-------------------------------

Build and Deploy a Python App to Amazon in 30 minutes

Setup
--------

Install Fabric, Flask and Boto

::

	pip install fabric flask boto


Create a Local Settings File that Stores Amazon settings

Sample File: local_settings.py
::

	# These are fake values
	aws_key = 'DFGT765UYYKAKIAJ4HFA'
	aws_secret = 'ASklKUYljkja97Kjk+adsasd/adsdssdsds'
	aws_rsa_key = '/home/foobar/.ssh/aws_keypair.pem'
	aws_security_groups = ['my_security_group']
	aws_key_pair = 'my_keypair_name'
	github_user = 'my_github_name'



