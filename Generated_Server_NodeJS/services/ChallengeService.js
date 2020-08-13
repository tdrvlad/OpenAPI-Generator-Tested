/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Archive shard from challenges
* Multiple status values can be provided with comma separated strings
*
* challengeId String The identifier of the challenge
* shard Integer The identifier of the shard
* force Boolean  (optional)
* returns ArchivedShard
* */
const archiveShard = ({ challengeId, shard, force }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
        shard,
        force,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Get archive list from challenges
* Multiple status values can be provided with comma separated strings
*
* challengeId String The identifier of the challenge
* returns List
* */
const archivedShardList = ({ challengeId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Assign a private challenge.
*
* assignUsersRequest AssignUsersRequest The users to be assigned to a challenge
* no response value expected for this operation
* */
const assignChallenge = ({ assignUsersRequest }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        assignUsersRequest,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Star a public challenge.
*
* challengeId String 
* tenantId String 
* no response value expected for this operation
* */
const assignTenantToChallenge = ({ challengeId, tenantId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
        tenantId,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Create a new challenge.
*
* challenge Challenge The challenge object to be created
* returns Challenge
* */
const createChallenge = ({ challenge }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challenge,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Download tagged items from challenges
* Multiple status values can be provided with comma separated strings
*
* challengeId String The identifier of the challenge
* shard Integer The identifier of the shard
* xAuthCredential String  (optional)
* no response value expected for this operation
* */
const downloadChallenge = ({ challengeId, shard, xAuthCredential }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
        shard,
        xAuthCredential,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* force merge
* Multiple status values can be provided with comma separated strings
*
* challengeId String The identifier of the dataset
* challengeName String The identifier of the tagged media item (optional)
* returns Challenge
* */
const forceMergeTaggedMediaItem = ({ challengeId, challengeName }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
        challengeName,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Retrieve list of challenges
* Multiple status values can be provided with comma separated strings
*
* challengeId String The identifier of the dataset
* accessToken String  (optional)
* returns Challenge
* */
const getChallenge = ({ challengeId, accessToken }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
        accessToken,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* get estimated cost for challenge
* estimage challenge budget
*
* challengeBudgetRequest ChallengeBudgetRequest The challenge options
* returns ChallengeBudgetResponse
* */
const getChallengeCost = ({ challengeBudgetRequest }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeBudgetRequest,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Retrieve list of challenges
* Multiple status values can be provided with comma separated strings
*
* challengeName String  (optional)
* accessType String  (optional)
* liked Boolean  (optional)
* pageSize Integer  (optional)
* pageNumber Integer  (optional)
* returns List
* */
const getChallengeListBroker = ({ challengeName, accessType, liked, pageSize, pageNumber }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeName,
        accessType,
        liked,
        pageSize,
        pageNumber,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Retrieve list of challenges
* Multiple status values can be provided with comma separated strings
*
* challengeName String  (optional)
* accessType String  (optional)
* liked Boolean  (optional)
* pageSize Integer  (optional)
* pageNumber Integer  (optional)
* returns List
* */
const getChallengeListCollaborator = ({ challengeName, accessType, liked, pageSize, pageNumber }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeName,
        accessType,
        liked,
        pageSize,
        pageNumber,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Retrieve list of challenges
* Multiple status values can be provided with comma separated strings
*
* challengeName String  (optional)
* accessType String  (optional)
* liked Boolean  (optional)
* pageSize Integer  (optional)
* pageNumber Integer  (optional)
* returns List
* */
const getChallengeListSupervisor = ({ challengeName, accessType, liked, pageSize, pageNumber }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeName,
        accessType,
        liked,
        pageSize,
        pageNumber,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Retrieve list tagged media items
* Multiple status values can be provided with comma separated strings
*
* challengeId String The identifier of the dataset
* pageSize Integer  (optional)
* pageNumber Integer  (optional)
* stage Integer  (optional)
* accessToken String  (optional)
* returns List
* */
const getTaggedItems = ({ challengeId, pageSize, pageNumber, stage, accessToken }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
        pageSize,
        pageNumber,
        stage,
        accessToken,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Update challenge.
*
* challengeId String The identifier of the dataset
* patchChallenge PatchChallenge The new challenge object
* returns Challenge
* */
const patchChallenge = ({ challengeId, patchChallenge }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
        patchChallenge,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Star a public challenge.
*
* challengeId String 
* body String The challenge object to be created
* no response value expected for this operation
* */
const rejectChallenge = ({ challengeId, body }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
        body,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Star a public challenge.
*
* challengeId String 
* no response value expected for this operation
* */
const starChallenge = ({ challengeId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Get challenge statistics
*
* challengeId String 
* returns ChallengeStatistics
* */
const statisticsChallenge = ({ challengeId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        challengeId,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);

module.exports = {
  archiveShard,
  archivedShardList,
  assignChallenge,
  assignTenantToChallenge,
  createChallenge,
  downloadChallenge,
  forceMergeTaggedMediaItem,
  getChallenge,
  getChallengeCost,
  getChallengeListBroker,
  getChallengeListCollaborator,
  getChallengeListSupervisor,
  getTaggedItems,
  patchChallenge,
  rejectChallenge,
  starChallenge,
  statisticsChallenge,
};
