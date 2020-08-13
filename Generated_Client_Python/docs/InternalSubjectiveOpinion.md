# InternalSubjectiveOpinion

Three independent counters corresponding to belief, disbelief and uncertainty. mediated by a common denominator and multiplied by a base rate (probability in the absence of this information).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opinion_emitter_id** | **str** | Functional source, if any, for this opinion, such a specific condition  | [optional] 
**opinion_reason_id** | **str** | Reason evoked, invoked or inferred by source for this opinion. | [optional] 
**attributed_belief_numerator** | **int** | Number, signed and additive, of fulfillment points out of total that are attributed to belief that the opinion is TRUE. belief mass (bx) numerator accumulator. | [optional] 
**attributed_disbelief_numerator** | **int** | Number, signed and additive, of fulfillment points out of total that are attributed to belief that the opinion is FALSE. belief mass (dx) numerator accumulator | [optional] 
**unattributed_uncertainty_numerator** | **int** | Number, signed and additive, of fulfillment points out of total that are unattributed to either belief or disbelief and thus represent uncertainty. uncertainty mass (ux) numerator accumulator. | [optional] 
**common_denominator** | **int** | The normalizing factor (the common denominator) of uncertainty, belief and disbelief. | [optional] 
**base_rate_numerator** | **int** | The probability of the opinion being true in the absence of the information generating it; this represents the default probability of a an element or character or letter appearing in a specific context | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


