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
    InternalSubjectiveOpinion,
    InternalSubjectiveOpinionFromJSON,
    InternalSubjectiveOpinionFromJSONTyped,
    InternalSubjectiveOpinionToJSON,
} from './';

/**
 * The object which described several possible values for a an observed character.
 * @export
 * @interface LatentSymbol
 */
export interface LatentSymbol {
    /**
     * 
     * @type {string}
     * @memberof LatentSymbol
     */
    value?: string;
    /**
     * 
     * @type {InternalSubjectiveOpinion}
     * @memberof LatentSymbol
     */
    subjectiveOpinion?: InternalSubjectiveOpinion;
}

export function LatentSymbolFromJSON(json: any): LatentSymbol {
    return LatentSymbolFromJSONTyped(json, false);
}

export function LatentSymbolFromJSONTyped(json: any, ignoreDiscriminator: boolean): LatentSymbol {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'value': !exists(json, 'value') ? undefined : json['value'],
        'subjectiveOpinion': !exists(json, 'subjectiveOpinion') ? undefined : InternalSubjectiveOpinionFromJSON(json['subjectiveOpinion']),
    };
}

export function LatentSymbolToJSON(value?: LatentSymbol | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'value': value.value,
        'subjectiveOpinion': InternalSubjectiveOpinionToJSON(value.subjectiveOpinion),
    };
}


