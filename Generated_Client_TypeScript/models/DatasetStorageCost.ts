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

import { exists, mapValues } from '../runtime';
import {
    DatasetTypeEnum,
    DatasetTypeEnumFromJSON,
    DatasetTypeEnumFromJSONTyped,
    DatasetTypeEnumToJSON,
} from './';

/**
 * 
 * @export
 * @interface DatasetStorageCost
 */
export interface DatasetStorageCost {
    /**
     * [TBD] Alpha-numeric, unique id of dataset
     * @type {string}
     * @memberof DatasetStorageCost
     */
    datasetId?: string;
    /**
     * 
     * @type {DatasetTypeEnum}
     * @memberof DatasetStorageCost
     */
    type?: DatasetTypeEnum;
    /**
     * cost for storage in dollars per month
     * @type {number}
     * @memberof DatasetStorageCost
     */
    estimatedShardCost?: number;
    /**
     * cost for storage in dollars per month
     * @type {number}
     * @memberof DatasetStorageCost
     */
    totalCost?: number;
}

export function DatasetStorageCostFromJSON(json: any): DatasetStorageCost {
    return DatasetStorageCostFromJSONTyped(json, false);
}

export function DatasetStorageCostFromJSONTyped(json: any, ignoreDiscriminator: boolean): DatasetStorageCost {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'datasetId': !exists(json, 'datasetId') ? undefined : json['datasetId'],
        'type': !exists(json, 'type') ? undefined : DatasetTypeEnumFromJSON(json['type']),
        'estimatedShardCost': !exists(json, 'estimatedShardCost') ? undefined : json['estimatedShardCost'],
        'totalCost': !exists(json, 'totalCost') ? undefined : json['totalCost'],
    };
}

export function DatasetStorageCostToJSON(value?: DatasetStorageCost | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'datasetId': value.datasetId,
        'type': DatasetTypeEnumToJSON(value.type),
        'estimatedShardCost': value.estimatedShardCost,
        'totalCost': value.totalCost,
    };
}


