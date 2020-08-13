from __future__ import print_function

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:3000"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
	
	# 1

	# Create an instance of the API class
	api_instance = openapi_client.ChallengeApi(api_client)
	challenge_id = 'challenge_id_example' # str | The identifier of the challenge
	shard = 56 # int | The identifier of the shard
	force = True # bool |  (optional)

	try:
	# Archive shard from challenges
		api_response = api_instance.archive_shard(challenge_id, shard, force=force)
		pprint(api_response)
	except ApiException as e:
		print("Exception when calling ChallengeApi->archive_shard: %s\n" % e)

	# 2

	# Create an instance of the API class
	api_instance = openapi_client.DatasetApi(api_client)
	dataset_id = '12y127'


	try:
	# Archive shard from challenges
		api_response = api_instance.get_dataset(dataset_id)
		pprint(api_response)
	except ApiException as e:
		print("Exception when calling ChallengeApi->archive_shard: %s\n" % e)
