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
/**
 * 
 * @export
 * @interface ChallengeDatasetMetadata
 */
export interface ChallengeDatasetMetadata {
    /**
     * [TBD] Alpha-numeric, name of dataset
     * @type {string}
     * @memberof ChallengeDatasetMetadata
     */
    name?: string;
    /**
     * estimated Tags Per Media Item
     * @type {number}
     * @memberof ChallengeDatasetMetadata
     */
    mediaItems?: number;
    /**
     * shards in dataset
     * @type {number}
     * @memberof ChallengeDatasetMetadata
     */
    numberOfShards?: number;
}

export function ChallengeDatasetMetadataFromJSON(json: any): ChallengeDatasetMetadata {
    return ChallengeDatasetMetadataFromJSONTyped(json, false);
}

export function ChallengeDatasetMetadataFromJSONTyped(json: any, ignoreDiscriminator: boolean): ChallengeDatasetMetadata {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': !exists(json, 'name') ? undefined : json['name'],
        'mediaItems': !exists(json, 'mediaItems') ? undefined : json['mediaItems'],
        'numberOfShards': !exists(json, 'numberOfShards') ? undefined : json['numberOfShards'],
    };
}

export function ChallengeDatasetMetadataToJSON(value?: ChallengeDatasetMetadata | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
        'mediaItems': value.mediaItems,
        'numberOfShards': value.numberOfShards,
    };
}


