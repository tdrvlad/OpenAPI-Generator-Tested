# MergedTag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merged_tag_id** | **str** | Alpha-numeric, unique id of tagged object | [optional] 
**media_item_id** | **str** | Alpha-numeric, unique id of tagged object | [optional] 
**challenge_id** | **str** | Alpha-numeric, unique id of tagged object | [optional] 
**permanent_identifier** | [**PermanentIdentifier**](PermanentIdentifier.md) |  | [optional] 
**node_type** | **str** | What type of object/event has been detected? | [optional] 
**geometry** | [**list[Shape]**](Shape.md) | What are the shapes that have been merged to determine this tag? | [optional] 
**evaluation** | [**Evaluation**](Evaluation.md) |  | [optional] 
**composing_tags** | **list[str]** | What are the tags which have been merged? | [optional] 
**evaluation_status** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


