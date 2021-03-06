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

/**
 * 
 * @export
 * @enum {string}
 */
export enum ShapeTypeEnum {
    Rectangle = '2D_rectangle',
    Polygon = '2D_polygon',
    RectangleTextBlock = '2D_rectangle_text_block',
    PolygonTextBlock = '2D_polygon_text_block',
    TimeboundPolygon = '2D_timebound_polygon'
}

export function ShapeTypeEnumFromJSON(json: any): ShapeTypeEnum {
    return ShapeTypeEnumFromJSONTyped(json, false);
}

export function ShapeTypeEnumFromJSONTyped(json: any, ignoreDiscriminator: boolean): ShapeTypeEnum {
    return json as ShapeTypeEnum;
}

export function ShapeTypeEnumToJSON(value?: ShapeTypeEnum | null): any {
    return value as any;
}

