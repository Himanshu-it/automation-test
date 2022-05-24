import os


env = os.getenv('TEST_ENV')
def test_create_primerx_patient():
	print('Running tests for env : ' + env)