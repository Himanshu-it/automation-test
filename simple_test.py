import os


env = os.getenv('TEST_ENV')
token_auth = os.getenv('TOKEN_AUTH_ENV')
def test_create_primerx_patient():
	if (not token_auth):
		print('Token auth is empty ')
	else:
		print('Token auth is not empty ')
	print('Running tests for env : ' + env + ' token is : ' + token_auth)