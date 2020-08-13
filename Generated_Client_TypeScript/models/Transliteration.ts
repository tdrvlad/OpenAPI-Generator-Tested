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
    ObservableSymbol,
    ObservableSymbolFromJSON,
    ObservableSymbolFromJSONTyped,
    ObservableSymbolToJSON,
} from './';

/**
 * Defines a segment of text associated to a Shape, together with many possibilities for each 
 * @export
 * @interface Transliteration
 */
export interface Transliteration {
    /**
     * The BCP-47 language code
     * @type {string}
     * @memberof Transliteration
     */
    languageCode?: string;
    /**
     * compressed version of character sequence
     * @type {string}
     * @memberof Transliteration
     */
    compressedCharacterSequence?: string;
    /**
     * Character encoding type
     * @type {string}
     * @memberof Transliteration
     */
    encoding?: TransliterationEncodingEnum;
    /**
     * The set of characters allowed , alphabet
     * @type {string}
     * @memberof Transliteration
     */
    charset?: TransliterationCharsetEnum;
    /**
     * reading direction
     * @type {string}
     * @memberof Transliteration
     */
    direction?: TransliterationDirectionEnum;
    /**
     * collation use for comparing and sorting the characters, as per Unicode Sorting Algorithm
     * @type {string}
     * @memberof Transliteration
     */
    collationLanguage?: TransliterationCollationLanguageEnum;
    /**
     * The order of the characters, according to the direction of the transliteration
     * @type {Array<ObservableSymbol>}
     * @memberof Transliteration
     */
    characterSequence?: Array<ObservableSymbol>;
}

export function TransliterationFromJSON(json: any): Transliteration {
    return TransliterationFromJSONTyped(json, false);
}

export function TransliterationFromJSONTyped(json: any, ignoreDiscriminator: boolean): Transliteration {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'languageCode': !exists(json, 'languageCode') ? undefined : json['languageCode'],
        'compressedCharacterSequence': !exists(json, 'compressedCharacterSequence') ? undefined : json['compressedCharacterSequence'],
        'encoding': !exists(json, 'encoding') ? undefined : json['encoding'],
        'charset': !exists(json, 'charset') ? undefined : json['charset'],
        'direction': !exists(json, 'direction') ? undefined : json['direction'],
        'collationLanguage': !exists(json, 'collation-language') ? undefined : json['collation-language'],
        'characterSequence': !exists(json, 'characterSequence') ? undefined : ((json['characterSequence'] as Array<any>).map(ObservableSymbolFromJSON)),
    };
}

export function TransliterationToJSON(value?: Transliteration | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'languageCode': value.languageCode,
        'compressedCharacterSequence': value.compressedCharacterSequence,
        'encoding': value.encoding,
        'charset': value.charset,
        'direction': value.direction,
        'collation-language': value.collationLanguage,
        'characterSequence': value.characterSequence === undefined ? undefined : ((value.characterSequence as Array<any>).map(ObservableSymbolToJSON)),
    };
}

/**
* @export
* @enum {string}
*/
export enum TransliterationEncodingEnum {
    ISO646ASCII = 'ISO-646-ASCII',
    UTF8 = 'UTF-8'
}
/**
* @export
* @enum {string}
*/
export enum TransliterationCharsetEnum {
    Latin1 = 'latin1',
    Latin2 = 'latin2',
    Cp1251 = 'cp1251',
    Greek = 'greek',
    Hebrew = 'hebrew'
}
/**
* @export
* @enum {string}
*/
export enum TransliterationDirectionEnum {
    LeftToRight = 'left-to-right',
    RightToLeft = 'right-to-left',
    TopToBottom = 'top-to-bottom',
    BottomToTop = 'bottom-to-top'
}
/**
* @export
* @enum {string}
*/
export enum TransliterationCollationLanguageEnum {
    Utf8RomanianCi = 'utf8_romanian_ci',
    Latin2GeneralCi = 'latin2_general_ci',
    Cp1250GeneralCi = 'cp1250_general_ci',
    GreekGeneralCi = 'greek_general_ci',
    HebrewGeneralCi = 'hebrew_general_ci'
}


