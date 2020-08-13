# PermanentIdentifierSegment

The object contains the description of an identifier segment
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding** | **str** | The encoding used for deserializing the value, before distance and identity functions can be computed | [optional] 
**index** | **int** | The index of the segment, so as to guarantee strict ordering of segment comparison | [optional] 
**weight** | **float** | The weight of the distance in the total distance | [optional] 
**assignment_function** | **str** | The hashcode obtained by running a SHA-512 on the binary values of the segments, in their order.  | [optional] 
**value** | **str** | The serialized value of the segment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


