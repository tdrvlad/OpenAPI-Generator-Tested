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
 * @interface ChallengeStatisticsUsersWorkTime
 */
export interface ChallengeStatisticsUsersWorkTime {
    /**
     *  avatar id
     * @type {string}
     * @memberof ChallengeStatisticsUsersWorkTime
     */
    name?: string;
    /**
     * 
     * @type {Array<Array<number>>}
     * @memberof ChallengeStatisticsUsersWorkTime
     */
    data?: Array<Array<number>>;
}

export function ChallengeStatisticsUsersWorkTimeFromJSON(json: any): ChallengeStatisticsUsersWorkTime {
    return ChallengeStatisticsUsersWorkTimeFromJSONTyped(json, false);
}

export function ChallengeStatisticsUsersWorkTimeFromJSONTyped(json: any, ignoreDiscriminator: boolean): ChallengeStatisticsUsersWorkTime {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': !exists(json, 'name') ? undefined : json['name'],
        'data': !exists(json, 'data') ? undefined : json['data'],
    };
}

export function ChallengeStatisticsUsersWorkTimeToJSON(value?: ChallengeStatisticsUsersWorkTime | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
        'data': value.data,
    };
}


