# Edge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_tag_id** | **str** | Need to find solution for unifying tag id&#39;s across taggers-collaborators.Alpha-numeric, unique id of tagged object | [optional] 
**destination_tag_id** | **str** | Need to find solution for unifying tag id&#39;s across taggers-collaborators. Alpha-numeric, unique id of tagged object | [optional] 
**source_text_box_id** | **str** | textBox id from inside sourceTag | [optional] 
**destination_text_box_id** | **str** | textBox id from inside destinationTag | [optional] 
**edge_type** | **str** | The type of the relationship between the two objects. Can be extended to discrete histogram of types. All types must belong to taxonomy or the challenge must allow for open-taxonomy. | [optional] 
**slack** | **float** | How much the edge can allow for the nodes to move without changing its length? | [optional] 
**elasticity** | **float** | How much the edge can extended or contracted? | [optional] 
**internal_subjective_opinion** | [**InternalSubjectiveOpinion**](InternalSubjectiveOpinion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


