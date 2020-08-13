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
    Edge,
    EdgeFromJSON,
    EdgeFromJSONTyped,
    EdgeToJSON,
    Image,
    ImageFromJSON,
    ImageFromJSONTyped,
    ImageToJSON,
    MergedTag,
    MergedTagFromJSON,
    MergedTagFromJSONTyped,
    MergedTagToJSON,
} from './';

/**
 * 
 * @export
 * @interface TaggedMediaItem
 */
export interface TaggedMediaItem {
    /**
     * Alpha-numeric, unique id of tagged object
     * @type {string}
     * @memberof TaggedMediaItem
     */
    taggedMediaItemId?: string;
    /**
     * Alpha-numeric, unique id of tagged object
     * @type {string}
     * @memberof TaggedMediaItem
     */
    mediaItemId?: string;
    /**
     * Alpha-numeric, unique id of tagged object
     * @type {string}
     * @memberof TaggedMediaItem
     */
    challengeId?: string;
    /**
     * What are the tasks contributed in the determination of these tags?
     * @type {Array<string>}
     * @memberof TaggedMediaItem
     */
    composingTasks?: Array<string>;
    /**
     * 
     * @type {Array<MergedTag>}
     * @memberof TaggedMediaItem
     */
    mergedTags?: Array<MergedTag>;
    /**
     * 
     * @type {Image}
     * @memberof TaggedMediaItem
     */
    image?: Image;
    /**
     * 
     * @type {Array<Edge>}
     * @memberof TaggedMediaItem
     */
    mergedEdges?: Array<Edge>;
}

export function TaggedMediaItemFromJSON(json: any): TaggedMediaItem {
    return TaggedMediaItemFromJSONTyped(json, false);
}

export function TaggedMediaItemFromJSONTyped(json: any, ignoreDiscriminator: boolean): TaggedMediaItem {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'taggedMediaItemId': !exists(json, 'taggedMediaItemId') ? undefined : json['taggedMediaItemId'],
        'mediaItemId': !exists(json, 'mediaItemId') ? undefined : json['mediaItemId'],
        'challengeId': !exists(json, 'challengeId') ? undefined : json['challengeId'],
        'composingTasks': !exists(json, 'composingTasks') ? undefined : json['composingTasks'],
        'mergedTags': !exists(json, 'mergedTags') ? undefined : ((json['mergedTags'] as Array<any>).map(MergedTagFromJSON)),
        'image': !exists(json, 'image') ? undefined : ImageFromJSON(json['image']),
        'mergedEdges': !exists(json, 'mergedEdges') ? undefined : ((json['mergedEdges'] as Array<any>).map(EdgeFromJSON)),
    };
}

export function TaggedMediaItemToJSON(value?: TaggedMediaItem | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'taggedMediaItemId': value.taggedMediaItemId,
        'mediaItemId': value.mediaItemId,
        'challengeId': value.challengeId,
        'composingTasks': value.composingTasks,
        'mergedTags': value.mergedTags === undefined ? undefined : ((value.mergedTags as Array<any>).map(MergedTagToJSON)),
        'image': ImageToJSON(value.image),
        'mergedEdges': value.mergedEdges === undefined ? undefined : ((value.mergedEdges as Array<any>).map(EdgeToJSON)),
    };
}


