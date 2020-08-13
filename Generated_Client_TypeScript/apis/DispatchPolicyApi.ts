/* tslint:disable */
/* eslint-disable */
/**
 * DeepVISS TAG
 * DeepVISS (Deep Vision Interoperability Specification Standard) allows several computer vision solutions to produce, consume and exchange events in the same format.
 *
 * The version of the OpenAPI document: 1.2.0
 * Contact: office@deepviss.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import {
    DispatchPolicy,
    DispatchPolicyFromJSON,
    DispatchPolicyToJSON,
} from '../models';

export interface CreateDispatchPolicyRequest {
    dispatchPolicy: DispatchPolicy;
}

/**
 * 
 */
export class DispatchPolicyApi extends runtime.BaseAPI {

    /**
     * Create a new dispatchPolicy.
     */
    async createDispatchPolicyRaw(requestParameters: CreateDispatchPolicyRequest): Promise<runtime.ApiResponse<DispatchPolicy>> {
        if (requestParameters.dispatchPolicy === null || requestParameters.dispatchPolicy === undefined) {
            throw new runtime.RequiredError('dispatchPolicy','Required parameter requestParameters.dispatchPolicy was null or undefined when calling createDispatchPolicy.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/dispatch-policy`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: DispatchPolicyToJSON(requestParameters.dispatchPolicy),
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => DispatchPolicyFromJSON(jsonValue));
    }

    /**
     * Create a new dispatchPolicy.
     */
    async createDispatchPolicy(requestParameters: CreateDispatchPolicyRequest): Promise<DispatchPolicy> {
        const response = await this.createDispatchPolicyRaw(requestParameters);
        return await response.value();
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of dispatch policies
     */
    async getDispatchPolicyListRaw(): Promise<runtime.ApiResponse<Array<DispatchPolicy>>> {
        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/dispatch-policy/list`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(DispatchPolicyFromJSON));
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of dispatch policies
     */
    async getDispatchPolicyList(): Promise<Array<DispatchPolicy>> {
        const response = await this.getDispatchPolicyListRaw();
        return await response.value();
    }

}
