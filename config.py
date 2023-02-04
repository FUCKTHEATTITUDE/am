import os
class Config(object):
	BOT_TOKEN = os.environ.get('BOT_TOKEN','5912024718:AAEH4ps9yHW3tLIf54oK8djR_3_Pg6yIUag')
	USERNAME = os.environ.get('USERNAME','sidharth')
	PASSWORD = os.environ.get('PASSWORD','WARP1d')
	TEAMSUSERNAME= os.environ.get('TEAMSUSERNAME')
	TEAMSPASSWORD= os.environ.get('TEAMSPASSWORD')
	#If above lines wont work then use below and pass credentials
	# BOT_TOKEN = os.environ.get('BOT_TOKEN','TELEGRAM_BOT_API_TOKEN')
	# USERNAME = os.environ.get('USERNAME','MAIL_ID')
	# PASSWORD = os.environ.get('PASSWORD','MAIL_PASSWORD')
	# TEAMSUSERNAME= os.environ.get('TEAMSUSERNAME','Teams mail id')
	# TEAMSPASSWORD= os.environ.get('TEAMSPASSWORD','teams password')
	
