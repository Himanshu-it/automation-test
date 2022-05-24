import os


env = os.getenv('TEST_ENV')
token_auth = os.getenv('TOKEN_AUTH_ENV')
def test_create_primerx_patient():
	print('Running tests for env : ' + env + ' token is : ' + token_auth)