import sys

try:
	from local_settings import aws_key, aws_secret, aws_key_path, aws_key_pair
	from local_settings import github_user
except:
	print """Error: You need to create a local_settings.py file
				 with your amazon secret variables!"""
	sys.exit(1)

# Github URL
REPO_URL = 'git@github.com:%s/thirty-min-app.git' % github_user

# Here lie the Amazon secrets
AWS = {
			'secrets' : {
				'aws_key' : aws_key,
				'aws_secret': aws_secret,
				'aws_key_path': aws_key_path,
			},
			'defaults' : {
					'image_id' : 'ami-aecd60c7',       # Amazon Linux 64-bit
					'instance_type' : 't1.micro',      # Micro Instance
					'security_groups': ['default'],    # Default Security Group
					'key_name': aws_key_pair,
			}
}

