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
 * @interface MediaDescriptor
 */
export interface MediaDescriptor {
    /**
     * Size of files when represented in binary, without additional encoding. Used for de-duplication.
     * @type {number}
     * @memberof MediaDescriptor
     */
    size?: number;
    /**
     * Cryptographic hash of original file. Used for de-duplication.
     * @type {string}
     * @memberof MediaDescriptor
     */
    hash?: string;
    /**
     * Perceptual representation of the content of the media. Used for de-duplication.
     * @type {string}
     * @memberof MediaDescriptor
     */
    pHash?: string;
}

export function MediaDescriptorFromJSON(json: any): MediaDescriptor {
    return MediaDescriptorFromJSONTyped(json, false);
}

export function MediaDescriptorFromJSONTyped(json: any, ignoreDiscriminator: boolean): MediaDescriptor {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'size': !exists(json, 'size') ? undefined : json['size'],
        'hash': !exists(json, 'hash') ? undefined : json['hash'],
        'pHash': !exists(json, 'pHash') ? undefined : json['pHash'],
    };
}

export function MediaDescriptorToJSON(value?: MediaDescriptor | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'size': value.size,
        'hash': value.hash,
        'pHash': value.pHash,
    };
}


