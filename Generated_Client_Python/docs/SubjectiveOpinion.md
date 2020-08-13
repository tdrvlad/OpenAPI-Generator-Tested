# SubjectiveOpinion

The reduced or collapsed version of InternalSubjectiveOpinion, with all beliefs and disbeliefs reduced per reason,emitter pair. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opinion_emitter_id** | **str** | Functional source, if any, for this opinion, such a specific condition or internal state encoutered. May be empty. | [optional] 
**opinion_reason_id** | **str** | Reason evoked, invoked or inferred by source for this opinion. May be empty. | [optional] 
**belief** | **float** | attributed to belief that the opinion is TRUE. belief mass (bx) normalized. | [optional] 
**disbelief** | **float** | attributed to belief that the opinion is FALSE. disbelief mass (dx)  normalized | [optional] 
**uncertainty** | **float** | unattributed to either belief or disbelief and thus represent uncertainty. uncertainty mass (ux) normalized. | [optional] 
**base_rate_probability** | **float** | The probability of the opinion being true in the absence of the information generating it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


