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


import * as runtime from '../runtime';
import {
    ArchivedShard,
    ArchivedShardFromJSON,
    ArchivedShardToJSON,
    AssignUsersRequest,
    AssignUsersRequestFromJSON,
    AssignUsersRequestToJSON,
    Challenge,
    ChallengeFromJSON,
    ChallengeToJSON,
    ChallengeBudgetRequest,
    ChallengeBudgetRequestFromJSON,
    ChallengeBudgetRequestToJSON,
    ChallengeBudgetResponse,
    ChallengeBudgetResponseFromJSON,
    ChallengeBudgetResponseToJSON,
    ChallengeStatistics,
    ChallengeStatisticsFromJSON,
    ChallengeStatisticsToJSON,
    PatchChallenge,
    PatchChallengeFromJSON,
    PatchChallengeToJSON,
    TaggedMediaItem,
    TaggedMediaItemFromJSON,
    TaggedMediaItemToJSON,
} from '../models';

export interface ArchiveShardRequest {
    challengeId: string;
    shard: number;
    force?: boolean;
}

export interface ArchivedShardListRequest {
    challengeId: string;
}

export interface AssignChallengeRequest {
    assignUsersRequest: AssignUsersRequest;
}

export interface AssignTenantToChallengeRequest {
    challengeId: string;
    tenantId: string;
}

export interface CreateChallengeRequest {
    challenge: Challenge;
}

export interface DownloadChallengeRequest {
    challengeId: string;
    shard: number;
    xAuthCredential?: string;
}

export interface ForceMergeTaggedMediaItemRequest {
    challengeId: string;
    challengeName?: string;
}

export interface GetChallengeRequest {
    challengeId: string;
    accessToken?: string;
}

export interface GetChallengeCostRequest {
    challengeBudgetRequest: ChallengeBudgetRequest;
}

export interface GetChallengeListBrokerRequest {
    challengeName?: string;
    accessType?: string;
    liked?: boolean;
    pageSize?: number;
    pageNumber?: number;
}

export interface GetChallengeListCollaboratorRequest {
    challengeName?: string;
    accessType?: string;
    liked?: boolean;
    pageSize?: number;
    pageNumber?: number;
}

export interface GetChallengeListSupervisorRequest {
    challengeName?: string;
    accessType?: string;
    liked?: boolean;
    pageSize?: number;
    pageNumber?: number;
}

export interface GetTaggedItemsRequest {
    challengeId: string;
    pageSize?: number;
    pageNumber?: number;
    stage?: number;
    accessToken?: string;
}

export interface PatchChallengeRequest {
    challengeId: string;
    patchChallenge: PatchChallenge;
}

export interface RejectChallengeRequest {
    challengeId: string;
    body: string;
}

export interface StarChallengeRequest {
    challengeId: string;
}

export interface StatisticsChallengeRequest {
    challengeId: string;
}

/**
 * 
 */
export class ChallengeApi extends runtime.BaseAPI {

    /**
     * Multiple status values can be provided with comma separated strings
     * Archive shard from challenges
     */
    async archiveShardRaw(requestParameters: ArchiveShardRequest): Promise<runtime.ApiResponse<ArchivedShard>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling archiveShard.');
        }

        if (requestParameters.shard === null || requestParameters.shard === undefined) {
            throw new runtime.RequiredError('shard','Required parameter requestParameters.shard was null or undefined when calling archiveShard.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.force !== undefined) {
            queryParameters['force'] = requestParameters.force;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/{challengeId}/archive/{shard}`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))).replace(`{${"shard"}}`, encodeURIComponent(String(requestParameters.shard))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => ArchivedShardFromJSON(jsonValue));
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Archive shard from challenges
     */
    async archiveShard(requestParameters: ArchiveShardRequest): Promise<ArchivedShard> {
        const response = await this.archiveShardRaw(requestParameters);
        return await response.value();
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Get archive list from challenges
     */
    async archivedShardListRaw(requestParameters: ArchivedShardListRequest): Promise<runtime.ApiResponse<Array<ArchivedShard>>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling archivedShardList.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/{challengeId}/archive/list`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(ArchivedShardFromJSON));
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Get archive list from challenges
     */
    async archivedShardList(requestParameters: ArchivedShardListRequest): Promise<Array<ArchivedShard>> {
        const response = await this.archivedShardListRaw(requestParameters);
        return await response.value();
    }

    /**
     * Assign a private challenge.
     */
    async assignChallengeRaw(requestParameters: AssignChallengeRequest): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.assignUsersRequest === null || requestParameters.assignUsersRequest === undefined) {
            throw new runtime.RequiredError('assignUsersRequest','Required parameter requestParameters.assignUsersRequest was null or undefined when calling assignChallenge.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/challenge/assign`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: AssignUsersRequestToJSON(requestParameters.assignUsersRequest),
        });

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Assign a private challenge.
     */
    async assignChallenge(requestParameters: AssignChallengeRequest): Promise<void> {
        await this.assignChallengeRaw(requestParameters);
    }

    /**
     * Star a public challenge.
     */
    async assignTenantToChallengeRaw(requestParameters: AssignTenantToChallengeRequest): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling assignTenantToChallenge.');
        }

        if (requestParameters.tenantId === null || requestParameters.tenantId === undefined) {
            throw new runtime.RequiredError('tenantId','Required parameter requestParameters.tenantId was null or undefined when calling assignTenantToChallenge.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/{challengeId}/assign-tenant/{tenantId}`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))).replace(`{${"tenantId"}}`, encodeURIComponent(String(requestParameters.tenantId))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Star a public challenge.
     */
    async assignTenantToChallenge(requestParameters: AssignTenantToChallengeRequest): Promise<void> {
        await this.assignTenantToChallengeRaw(requestParameters);
    }

    /**
     * Create a new challenge.
     */
    async createChallengeRaw(requestParameters: CreateChallengeRequest): Promise<runtime.ApiResponse<Challenge>> {
        if (requestParameters.challenge === null || requestParameters.challenge === undefined) {
            throw new runtime.RequiredError('challenge','Required parameter requestParameters.challenge was null or undefined when calling createChallenge.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/challenge`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: ChallengeToJSON(requestParameters.challenge),
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => ChallengeFromJSON(jsonValue));
    }

    /**
     * Create a new challenge.
     */
    async createChallenge(requestParameters: CreateChallengeRequest): Promise<Challenge> {
        const response = await this.createChallengeRaw(requestParameters);
        return await response.value();
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Download tagged items from challenges
     */
    async downloadChallengeRaw(requestParameters: DownloadChallengeRequest): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling downloadChallenge.');
        }

        if (requestParameters.shard === null || requestParameters.shard === undefined) {
            throw new runtime.RequiredError('shard','Required parameter requestParameters.shard was null or undefined when calling downloadChallenge.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.xAuthCredential !== undefined) {
            queryParameters['X-Auth-Credential'] = requestParameters.xAuthCredential;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/{challengeId}/download/{shard}`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))).replace(`{${"shard"}}`, encodeURIComponent(String(requestParameters.shard))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Download tagged items from challenges
     */
    async downloadChallenge(requestParameters: DownloadChallengeRequest): Promise<void> {
        await this.downloadChallengeRaw(requestParameters);
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * force merge
     */
    async forceMergeTaggedMediaItemRaw(requestParameters: ForceMergeTaggedMediaItemRequest): Promise<runtime.ApiResponse<Challenge>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling forceMergeTaggedMediaItem.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.challengeName !== undefined) {
            queryParameters['challengeName'] = requestParameters.challengeName;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/{challengeId}/force-merge`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => ChallengeFromJSON(jsonValue));
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * force merge
     */
    async forceMergeTaggedMediaItem(requestParameters: ForceMergeTaggedMediaItemRequest): Promise<Challenge> {
        const response = await this.forceMergeTaggedMediaItemRaw(requestParameters);
        return await response.value();
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of challenges
     */
    async getChallengeRaw(requestParameters: GetChallengeRequest): Promise<runtime.ApiResponse<Challenge>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling getChallenge.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.accessToken !== undefined) {
            queryParameters['accessToken'] = requestParameters.accessToken;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/{challengeId}`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => ChallengeFromJSON(jsonValue));
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of challenges
     */
    async getChallenge(requestParameters: GetChallengeRequest): Promise<Challenge> {
        const response = await this.getChallengeRaw(requestParameters);
        return await response.value();
    }

    /**
     * estimage challenge budget
     * get estimated cost for challenge
     */
    async getChallengeCostRaw(requestParameters: GetChallengeCostRequest): Promise<runtime.ApiResponse<ChallengeBudgetResponse>> {
        if (requestParameters.challengeBudgetRequest === null || requestParameters.challengeBudgetRequest === undefined) {
            throw new runtime.RequiredError('challengeBudgetRequest','Required parameter requestParameters.challengeBudgetRequest was null or undefined when calling getChallengeCost.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/challenge/cost`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: ChallengeBudgetRequestToJSON(requestParameters.challengeBudgetRequest),
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => ChallengeBudgetResponseFromJSON(jsonValue));
    }

    /**
     * estimage challenge budget
     * get estimated cost for challenge
     */
    async getChallengeCost(requestParameters: GetChallengeCostRequest): Promise<ChallengeBudgetResponse> {
        const response = await this.getChallengeCostRaw(requestParameters);
        return await response.value();
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of challenges
     */
    async getChallengeListBrokerRaw(requestParameters: GetChallengeListBrokerRequest): Promise<runtime.ApiResponse<Array<Challenge>>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.challengeName !== undefined) {
            queryParameters['challengeName'] = requestParameters.challengeName;
        }

        if (requestParameters.accessType !== undefined) {
            queryParameters['accessType'] = requestParameters.accessType;
        }

        if (requestParameters.liked !== undefined) {
            queryParameters['liked'] = requestParameters.liked;
        }

        if (requestParameters.pageSize !== undefined) {
            queryParameters['pageSize'] = requestParameters.pageSize;
        }

        if (requestParameters.pageNumber !== undefined) {
            queryParameters['pageNumber'] = requestParameters.pageNumber;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/broker/list`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(ChallengeFromJSON));
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of challenges
     */
    async getChallengeListBroker(requestParameters: GetChallengeListBrokerRequest): Promise<Array<Challenge>> {
        const response = await this.getChallengeListBrokerRaw(requestParameters);
        return await response.value();
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of challenges
     */
    async getChallengeListCollaboratorRaw(requestParameters: GetChallengeListCollaboratorRequest): Promise<runtime.ApiResponse<Array<Challenge>>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.challengeName !== undefined) {
            queryParameters['challengeName'] = requestParameters.challengeName;
        }

        if (requestParameters.accessType !== undefined) {
            queryParameters['accessType'] = requestParameters.accessType;
        }

        if (requestParameters.liked !== undefined) {
            queryParameters['liked'] = requestParameters.liked;
        }

        if (requestParameters.pageSize !== undefined) {
            queryParameters['pageSize'] = requestParameters.pageSize;
        }

        if (requestParameters.pageNumber !== undefined) {
            queryParameters['pageNumber'] = requestParameters.pageNumber;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/collaborator/list`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(ChallengeFromJSON));
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of challenges
     */
    async getChallengeListCollaborator(requestParameters: GetChallengeListCollaboratorRequest): Promise<Array<Challenge>> {
        const response = await this.getChallengeListCollaboratorRaw(requestParameters);
        return await response.value();
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of challenges
     */
    async getChallengeListSupervisorRaw(requestParameters: GetChallengeListSupervisorRequest): Promise<runtime.ApiResponse<Array<Challenge>>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.challengeName !== undefined) {
            queryParameters['challengeName'] = requestParameters.challengeName;
        }

        if (requestParameters.accessType !== undefined) {
            queryParameters['accessType'] = requestParameters.accessType;
        }

        if (requestParameters.liked !== undefined) {
            queryParameters['liked'] = requestParameters.liked;
        }

        if (requestParameters.pageSize !== undefined) {
            queryParameters['pageSize'] = requestParameters.pageSize;
        }

        if (requestParameters.pageNumber !== undefined) {
            queryParameters['pageNumber'] = requestParameters.pageNumber;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/supervisor/list`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(ChallengeFromJSON));
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list of challenges
     */
    async getChallengeListSupervisor(requestParameters: GetChallengeListSupervisorRequest): Promise<Array<Challenge>> {
        const response = await this.getChallengeListSupervisorRaw(requestParameters);
        return await response.value();
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list tagged media items
     */
    async getTaggedItemsRaw(requestParameters: GetTaggedItemsRequest): Promise<runtime.ApiResponse<Array<TaggedMediaItem>>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling getTaggedItems.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.pageSize !== undefined) {
            queryParameters['pageSize'] = requestParameters.pageSize;
        }

        if (requestParameters.pageNumber !== undefined) {
            queryParameters['pageNumber'] = requestParameters.pageNumber;
        }

        if (requestParameters.stage !== undefined) {
            queryParameters['stage'] = requestParameters.stage;
        }

        if (requestParameters.accessToken !== undefined) {
            queryParameters['accessToken'] = requestParameters.accessToken;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/{challengeId}/tagged-item/list`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(TaggedMediaItemFromJSON));
    }

    /**
     * Multiple status values can be provided with comma separated strings
     * Retrieve list tagged media items
     */
    async getTaggedItems(requestParameters: GetTaggedItemsRequest): Promise<Array<TaggedMediaItem>> {
        const response = await this.getTaggedItemsRaw(requestParameters);
        return await response.value();
    }

    /**
     * Update challenge.
     */
    async patchChallengeRaw(requestParameters: PatchChallengeRequest): Promise<runtime.ApiResponse<Challenge>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling patchChallenge.');
        }

        if (requestParameters.patchChallenge === null || requestParameters.patchChallenge === undefined) {
            throw new runtime.RequiredError('patchChallenge','Required parameter requestParameters.patchChallenge was null or undefined when calling patchChallenge.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/challenge/{challengeId}`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))),
            method: 'PATCH',
            headers: headerParameters,
            query: queryParameters,
            body: PatchChallengeToJSON(requestParameters.patchChallenge),
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => ChallengeFromJSON(jsonValue));
    }

    /**
     * Update challenge.
     */
    async patchChallenge(requestParameters: PatchChallengeRequest): Promise<Challenge> {
        const response = await this.patchChallengeRaw(requestParameters);
        return await response.value();
    }

    /**
     * Star a public challenge.
     */
    async rejectChallengeRaw(requestParameters: RejectChallengeRequest): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling rejectChallenge.');
        }

        if (requestParameters.body === null || requestParameters.body === undefined) {
            throw new runtime.RequiredError('body','Required parameter requestParameters.body was null or undefined when calling rejectChallenge.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/challenge/{challengeId}/reject`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: requestParameters.body as any,
        });

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Star a public challenge.
     */
    async rejectChallenge(requestParameters: RejectChallengeRequest): Promise<void> {
        await this.rejectChallengeRaw(requestParameters);
    }

    /**
     * Star a public challenge.
     */
    async starChallengeRaw(requestParameters: StarChallengeRequest): Promise<runtime.ApiResponse<void>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling starChallenge.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/{challengeId}/star`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.VoidApiResponse(response);
    }

    /**
     * Star a public challenge.
     */
    async starChallenge(requestParameters: StarChallengeRequest): Promise<void> {
        await this.starChallengeRaw(requestParameters);
    }

    /**
     * Get challenge statistics
     */
    async statisticsChallengeRaw(requestParameters: StatisticsChallengeRequest): Promise<runtime.ApiResponse<ChallengeStatistics>> {
        if (requestParameters.challengeId === null || requestParameters.challengeId === undefined) {
            throw new runtime.RequiredError('challengeId','Required parameter requestParameters.challengeId was null or undefined when calling statisticsChallenge.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/challenge/{challengeId}/statistics`.replace(`{${"challengeId"}}`, encodeURIComponent(String(requestParameters.challengeId))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.JSONApiResponse(response, (jsonValue) => ChallengeStatisticsFromJSON(jsonValue));
    }

    /**
     * Get challenge statistics
     */
    async statisticsChallenge(requestParameters: StatisticsChallengeRequest): Promise<ChallengeStatistics> {
        const response = await this.statisticsChallengeRaw(requestParameters);
        return await response.value();
    }

}