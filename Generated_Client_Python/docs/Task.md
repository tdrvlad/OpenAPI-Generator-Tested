# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Alpha-numeric, unique id of user who has performed the task | [optional] 
**avatar_id** | **str** | Alpha-numeric, unique id of user who has performed the task. | [optional] 
**challenge_id** | **str** | Alpa-numeric, unique id of challenge.  | [optional] 
**attempt_sequence_number** | **int** | Identifies the number of evaluation attempts performed on this specific media item. | [optional] 
**generation_timestamp** | **datetime** | Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00) when the task was requested by the user | [optional] 
**submission_timestamp** | **datetime** | Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00) when the task was submitted by the user | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**evaluation_status** | **str** |  | [optional] 
**challenge_name** | **str** | Name of Challenge | [optional] 
**challenge_description** | **str** | [TBD] Alpha-numeric, name of dataset | [optional] 
**tags** | [**list[Tag]**](Tag.md) |  | [optional] 
**edges** | [**list[Edge]**](Edge.md) |  | [optional] 
**resolution** | [**TaskResolution**](TaskResolution.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


