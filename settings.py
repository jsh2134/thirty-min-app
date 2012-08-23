import sys

try:
	from local_settings import aws_key, aws_secret, aws_key_pair
except:
	print """Error: You need to create a local_settings.py file
				 with your amazon secret variables!"""
	sys.exit(1)


# Here lie the settings
REPO_URL = 'git@github.com:jsh2134/test-app.git'

# Here lie the secrets
SECRETS = {
			'aws_key' : aws_key,
			'aws_secret': aws_secret,
			'aws_key_pair': aws_key_pair
}

