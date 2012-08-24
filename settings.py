import sys

try:
	from local_settings import aws_key, aws_secret, aws_rsa_key
	from local_settings import aws_security_groups, aws_key_pair
	from local_settings import github_user
except:
	print """Error: You need to create a local_settings.py file
				 with your amazon secret variables!"""
	sys.exit(1)

# Github URL
REPO_URL = 'git@github.com:%s/thirty-min-app.git' % github_user

# Here lie the Amazon secrets
SECRETS = {
			'aws_key' : aws_key,
			'aws_secret': aws_secret,
			'aws_rsa_key': aws_rsa_key,
			'aws_security_groups': aws_security_groups,
			'aws_key_pair': aws_key_pair
}

