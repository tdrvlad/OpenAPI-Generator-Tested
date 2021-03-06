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
 * Information about a task
 * @export
 * @interface TaskResolution
 */
export interface TaskResolution {
    /**
     * description
     * @type {string}
     * @memberof TaskResolution
     */
    description?: string;
}

export function TaskResolutionFromJSON(json: any): TaskResolution {
    return TaskResolutionFromJSONTyped(json, false);
}

export function TaskResolutionFromJSONTyped(json: any, ignoreDiscriminator: boolean): TaskResolution {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'description': !exists(json, 'description') ? undefined : json['description'],
    };
}

export function TaskResolutionToJSON(value?: TaskResolution | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'description': value.description,
    };
}


