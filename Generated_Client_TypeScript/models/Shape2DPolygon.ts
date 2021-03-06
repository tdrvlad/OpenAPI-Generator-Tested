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
    Point2D,
    Point2DFromJSON,
    Point2DFromJSONTyped,
    Point2DToJSON,
    Shape,
    ShapeFromJSON,
    ShapeFromJSONTyped,
    ShapeToJSON,
    Shape2DPolygonAllOf,
    Shape2DPolygonAllOfFromJSON,
    Shape2DPolygonAllOfFromJSONTyped,
    Shape2DPolygonAllOfToJSON,
} from './';

/**
 * 
 * @export
 * @interface Shape2DPolygon
 */
export interface Shape2DPolygon extends Shape {
    /**
     * 
     * @type {Array<Point2D>}
     * @memberof Shape2DPolygon
     */
    points?: Array<Point2D>;
}

export function Shape2DPolygonFromJSON(json: any): Shape2DPolygon {
    return Shape2DPolygonFromJSONTyped(json, false);
}

export function Shape2DPolygonFromJSONTyped(json: any, ignoreDiscriminator: boolean): Shape2DPolygon {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        ...ShapeFromJSONTyped(json, ignoreDiscriminator),
        'points': !exists(json, 'points') ? undefined : ((json['points'] as Array<any>).map(Point2DFromJSON)),
    };
}

export function Shape2DPolygonToJSON(value?: Shape2DPolygon | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        ...ShapeToJSON(value),
        'points': value.points === undefined ? undefined : ((value.points as Array<any>).map(Point2DToJSON)),
    };
}


