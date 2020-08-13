# EvaluationPolicy

The parameters used in the evaluation of a challenge, its tasks and their Tags.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_policy_id** | **str** | Unique ID of evaluation policy | [optional] 
**name** | **str** | name | [optional] 
**spatial_overlap_threshold** | **float** | The minimum amount of overlap between two tags, which, in conjuction with a matching object-type, is a condition for merging two tags | [optional] 
**harshness** | **float** | The penalty incurred for a tag that is NOT matched with other tags | [optional] 
**rank_of_mean** | **float** | The rank (power) of the generalized mean used for evaluating a task composed of several tags. Negative values mean harsher evaluations, values larger than 1.0 mean less harsh evaluations. Default value is 1.0 (arithmetic mean).  | [optional] 
**summation_type** | **str** | If set to &#39;algebraic&#39;, negative results on one task will be substracted from user payout. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


