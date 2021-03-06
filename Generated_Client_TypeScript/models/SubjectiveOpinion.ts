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
 * The reduced or collapsed version of InternalSubjectiveOpinion, with all beliefs and disbeliefs reduced per reason,emitter pair. 
 * @export
 * @interface SubjectiveOpinion
 */
export interface SubjectiveOpinion {
    /**
     * Functional source, if any, for this opinion, such a specific condition or internal state encoutered. May be empty.
     * @type {string}
     * @memberof SubjectiveOpinion
     */
    opinionEmitterId?: string;
    /**
     * Reason evoked, invoked or inferred by source for this opinion. May be empty.
     * @type {string}
     * @memberof SubjectiveOpinion
     */
    opinionReasonId?: string;
    /**
     * attributed to belief that the opinion is TRUE. belief mass (bx) normalized.
     * @type {number}
     * @memberof SubjectiveOpinion
     */
    belief?: number;
    /**
     * attributed to belief that the opinion is FALSE. disbelief mass (dx)  normalized
     * @type {number}
     * @memberof SubjectiveOpinion
     */
    disbelief?: number;
    /**
     * unattributed to either belief or disbelief and thus represent uncertainty. uncertainty mass (ux) normalized.
     * @type {number}
     * @memberof SubjectiveOpinion
     */
    uncertainty?: number;
    /**
     * The probability of the opinion being true in the absence of the information generating it.
     * @type {number}
     * @memberof SubjectiveOpinion
     */
    baseRateProbability?: number;
}

export function SubjectiveOpinionFromJSON(json: any): SubjectiveOpinion {
    return SubjectiveOpinionFromJSONTyped(json, false);
}

export function SubjectiveOpinionFromJSONTyped(json: any, ignoreDiscriminator: boolean): SubjectiveOpinion {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'opinionEmitterId': !exists(json, 'opinionEmitterId') ? undefined : json['opinionEmitterId'],
        'opinionReasonId': !exists(json, 'opinionReasonId') ? undefined : json['opinionReasonId'],
        'belief': !exists(json, 'belief') ? undefined : json['belief'],
        'disbelief': !exists(json, 'disbelief') ? undefined : json['disbelief'],
        'uncertainty': !exists(json, 'uncertainty') ? undefined : json['uncertainty'],
        'baseRateProbability': !exists(json, 'baseRateProbability') ? undefined : json['baseRateProbability'],
    };
}

export function SubjectiveOpinionToJSON(value?: SubjectiveOpinion | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'opinionEmitterId': value.opinionEmitterId,
        'opinionReasonId': value.opinionReasonId,
        'belief': value.belief,
        'disbelief': value.disbelief,
        'uncertainty': value.uncertainty,
        'baseRateProbability': value.baseRateProbability,
    };
}


