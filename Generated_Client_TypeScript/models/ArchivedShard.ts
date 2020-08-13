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
 * @interface ArchivedShard
 */
export interface ArchivedShard {
    /**
     * Alpha-numeric, unique id of challenge. 
     * @type {string}
     * @memberof ArchivedShard
     */
    challengeId?: string;
    /**
     * TBD
     * @type {number}
     * @memberof ArchivedShard
     */
    shard?: number;
    /**
     * name of the archived shard
     * @type {string}
     * @memberof ArchivedShard
     */
    archiveName?: string;
    /**
     * Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)
     * @type {Date}
     * @memberof ArchivedShard
     */
    creationTimestamp?: Date;
    /**
     * Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00)
     * @type {Date}
     * @memberof ArchivedShard
     */
    lastUpdateTimestamp?: Date;
    /**
     * completion percentage of a challenge
     * @type {number}
     * @memberof ArchivedShard
     */
    archiveCompletionPercentage?: number;
    /**
     * completion percentage of a challenge
     * @type {number}
     * @memberof ArchivedShard
     */
    currentCompletionPercentage?: number;
}

export function ArchivedShardFromJSON(json: any): ArchivedShard {
    return ArchivedShardFromJSONTyped(json, false);
}

export function ArchivedShardFromJSONTyped(json: any, ignoreDiscriminator: boolean): ArchivedShard {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'challengeId': !exists(json, 'challengeId') ? undefined : json['challengeId'],
        'shard': !exists(json, 'shard') ? undefined : json['shard'],
        'archiveName': !exists(json, 'archiveName') ? undefined : json['archiveName'],
        'creationTimestamp': !exists(json, 'creationTimestamp') ? undefined : (new Date(json['creationTimestamp'])),
        'lastUpdateTimestamp': !exists(json, 'lastUpdateTimestamp') ? undefined : (new Date(json['lastUpdateTimestamp'])),
        'archiveCompletionPercentage': !exists(json, 'archiveCompletionPercentage') ? undefined : json['archiveCompletionPercentage'],
        'currentCompletionPercentage': !exists(json, 'currentCompletionPercentage') ? undefined : json['currentCompletionPercentage'],
    };
}

export function ArchivedShardToJSON(value?: ArchivedShard | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'challengeId': value.challengeId,
        'shard': value.shard,
        'archiveName': value.archiveName,
        'creationTimestamp': value.creationTimestamp === undefined ? undefined : (value.creationTimestamp.toISOString()),
        'lastUpdateTimestamp': value.lastUpdateTimestamp === undefined ? undefined : (value.lastUpdateTimestamp.toISOString()),
        'archiveCompletionPercentage': value.archiveCompletionPercentage,
        'currentCompletionPercentage': value.currentCompletionPercentage,
    };
}


