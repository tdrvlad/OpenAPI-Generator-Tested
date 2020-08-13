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
    Tag,
    TagFromJSON,
    TagFromJSONTyped,
    TagToJSON,
    TaskResolution,
    TaskResolutionFromJSON,
    TaskResolutionFromJSONTyped,
    TaskResolutionToJSON,
} from './';

/**
 * 
 * @export
 * @interface Task
 */
export interface Task {
    /**
     * Alpha-numeric, unique id of user who has performed the task
     * @type {string}
     * @memberof Task
     */
    taskId?: string;
    /**
     * Alpha-numeric, unique id of user who has performed the task.
     * @type {string}
     * @memberof Task
     */
    avatarId?: string;
    /**
     * Alpa-numeric, unique id of challenge. 
     * @type {string}
     * @memberof Task
     */
    challengeId?: string;
    /**
     * Identifies the number of evaluation attempts performed on this specific media item.
     * @type {number}
     * @memberof Task
     */
    attemptSequenceNumber?: number;
    /**
     * Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00) when the task was requested by the user
     * @type {Date}
     * @memberof Task
     */
    generationTimestamp?: Date;
    /**
     * Date and time expressed according to ISO 8601 (e.g. 2018-06-24T23:10:28+03:00) when the task was submitted by the user
     * @type {Date}
     * @memberof Task
     */
    submissionTimestamp?: Date;
    /**
     * 
     * @type {Image}
     * @memberof Task
     */
    image?: Image;
    /**
     * 
     * @type {string}
     * @memberof Task
     */
    evaluationStatus?: TaskEvaluationStatusEnum;
    /**
     * Name of Challenge
     * @type {string}
     * @memberof Task
     */
    challengeName?: string;
    /**
     * [TBD] Alpha-numeric, name of dataset
     * @type {string}
     * @memberof Task
     */
    challengeDescription?: string;
    /**
     * 
     * @type {Array<Tag>}
     * @memberof Task
     */
    tags?: Array<Tag>;
    /**
     * 
     * @type {Array<Edge>}
     * @memberof Task
     */
    edges?: Array<Edge>;
    /**
     * 
     * @type {TaskResolution}
     * @memberof Task
     */
    resolution?: TaskResolution;
}

export function TaskFromJSON(json: any): Task {
    return TaskFromJSONTyped(json, false);
}

export function TaskFromJSONTyped(json: any, ignoreDiscriminator: boolean): Task {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'taskId': !exists(json, 'taskId') ? undefined : json['taskId'],
        'avatarId': !exists(json, 'avatarId') ? undefined : json['avatarId'],
        'challengeId': !exists(json, 'challengeId') ? undefined : json['challengeId'],
        'attemptSequenceNumber': !exists(json, 'attemptSequenceNumber') ? undefined : json['attemptSequenceNumber'],
        'generationTimestamp': !exists(json, 'generationTimestamp') ? undefined : (new Date(json['generationTimestamp'])),
        'submissionTimestamp': !exists(json, 'submissionTimestamp') ? undefined : (new Date(json['submissionTimestamp'])),
        'image': !exists(json, 'image') ? undefined : ImageFromJSON(json['image']),
        'evaluationStatus': !exists(json, 'evaluationStatus') ? undefined : json['evaluationStatus'],
        'challengeName': !exists(json, 'challengeName') ? undefined : json['challengeName'],
        'challengeDescription': !exists(json, 'challengeDescription') ? undefined : json['challengeDescription'],
        'tags': !exists(json, 'tags') ? undefined : ((json['tags'] as Array<any>).map(TagFromJSON)),
        'edges': !exists(json, 'edges') ? undefined : ((json['edges'] as Array<any>).map(EdgeFromJSON)),
        'resolution': !exists(json, 'resolution') ? undefined : TaskResolutionFromJSON(json['resolution']),
    };
}

export function TaskToJSON(value?: Task | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'taskId': value.taskId,
        'avatarId': value.avatarId,
        'challengeId': value.challengeId,
        'attemptSequenceNumber': value.attemptSequenceNumber,
        'generationTimestamp': value.generationTimestamp === undefined ? undefined : (value.generationTimestamp.toISOString()),
        'submissionTimestamp': value.submissionTimestamp === undefined ? undefined : (value.submissionTimestamp.toISOString()),
        'image': ImageToJSON(value.image),
        'evaluationStatus': value.evaluationStatus,
        'challengeName': value.challengeName,
        'challengeDescription': value.challengeDescription,
        'tags': value.tags === undefined ? undefined : ((value.tags as Array<any>).map(TagToJSON)),
        'edges': value.edges === undefined ? undefined : ((value.edges as Array<any>).map(EdgeToJSON)),
        'resolution': TaskResolutionToJSON(value.resolution),
    };
}

/**
* @export
* @enum {string}
*/
export enum TaskEvaluationStatusEnum {
    Unallocated = 'unallocated',
    Leased = 'leased',
    NotEvaluated = 'not-evaluated',
    Passed = 'passed',
    Failed = 'failed',
    Skipped = 'skipped',
    TimedOut = 'timed-out',
    PermamnentlyFailed = 'permamnently-failed'
}

