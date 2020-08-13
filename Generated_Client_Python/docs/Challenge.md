# Challenge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_id** | **str** | Alpha-numeric, unique id of challenge.  | [optional] 
**dataset_id** | **str** | Alpha-numeric, unique id of dataset | [optional] 
**evaluation_policy_id** | **str** | Alpha-numeric, unique id of evaluation policy | [optional] 
**dispatch_policy_id** | **str** | Alpha-numeric, unique id of dispatch policy | [optional] 
**creation_timestamp** | **datetime** | Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00) | [optional] 
**status** | [**ChallengeStatusEnum**](ChallengeStatusEnum.md) |  | [optional] 
**access_type** | [**ChallengeAccessTypeEnum**](ChallengeAccessTypeEnum.md) |  | 
**tenant_role** | [**ChallengeTenantRoleEnum**](ChallengeTenantRoleEnum.md) |  | [optional] 
**name** | **str** | [TBD] Alpha-numeric, name of dataset | [optional] 
**completion_percentage** | **int** | completion percentage of a challenge | [optional] 
**completion_percentage_for_collaborator** | **int** | completion percentage of a challenge for a collaborator | [optional] 
**description** | **str** | [TBD] Alpha-numeric, name of dataset | [optional] 
**budget** | **float** | budget allocated for challenge | [optional] 
**stared** | **bool** | [TBD] Alpha-numeric, name of dataset | [optional] 
**supplier_tenant_id** | **str** | [TBD] Alpha-numeric, name of supplierTenantId | [optional] 
**resolution** | **str** | [TBD] Alpha-numeric, name of dataset | [optional] 
**demander_tenant_id** | **str** | [TBD] Alpha-numeric, name of demanderTenantId | [optional] 
**initial_number_of_shards** | **int** | shards in dataset | [optional] 
**dataset_metadata** | [**ChallengeDatasetMetadata**](ChallengeDatasetMetadata.md) |  | [optional] 
**tag_type** | [**ShapeTypeEnum**](ShapeTypeEnum.md) |  | [optional] 
**estimated_tags_per_media_item** | **float** | estimated Tags Per Media Item | [optional] 
**node_taxonomy** | **list[str]** | taxonomy list for nodeType | [optional] 
**edge_taxonomy** | **list[str]** | taxonomy list for edgeType | [optional] 
**completion_percentages** | [**list[ChallengeCompletionPercentage]**](ChallengeCompletionPercentage.md) |  | [optional] 
**expiration** | **int** | hours until the challenge is expired | [optional] 
**challenge_access_token** | **str** | Token for accessing the challenge | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


