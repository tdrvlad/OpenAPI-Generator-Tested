/**
 * The ChallengeController file is a very simple one, which does not need to be changed manually,
 * unless there's a case where business logic reoutes the request to an entity which is not
 * the service.
 * The heavy lifting of the Controller item is done in Request.js - that is where request
 * parameters are extracted and sent to the service, and where response is handled.
 */

const Controller = require('./Controller');
const service = require('../services/ChallengeService');
const archiveShard = async (request, response) => {
  await Controller.handleRequest(request, response, service.archiveShard);
};

const archivedShardList = async (request, response) => {
  await Controller.handleRequest(request, response, service.archivedShardList);
};

const assignChallenge = async (request, response) => {
  await Controller.handleRequest(request, response, service.assignChallenge);
};

const assignTenantToChallenge = async (request, response) => {
  await Controller.handleRequest(request, response, service.assignTenantToChallenge);
};

const createChallenge = async (request, response) => {
  await Controller.handleRequest(request, response, service.createChallenge);
};

const downloadChallenge = async (request, response) => {
  await Controller.handleRequest(request, response, service.downloadChallenge);
};

const forceMergeTaggedMediaItem = async (request, response) => {
  await Controller.handleRequest(request, response, service.forceMergeTaggedMediaItem);
};

const getChallenge = async (request, response) => {
  await Controller.handleRequest(request, response, service.getChallenge);
};

const getChallengeCost = async (request, response) => {
  await Controller.handleRequest(request, response, service.getChallengeCost);
};

const getChallengeListBroker = async (request, response) => {
  await Controller.handleRequest(request, response, service.getChallengeListBroker);
};

const getChallengeListCollaborator = async (request, response) => {
  await Controller.handleRequest(request, response, service.getChallengeListCollaborator);
};

const getChallengeListSupervisor = async (request, response) => {
  await Controller.handleRequest(request, response, service.getChallengeListSupervisor);
};

const getTaggedItems = async (request, response) => {
  await Controller.handleRequest(request, response, service.getTaggedItems);
};

const patchChallenge = async (request, response) => {
  await Controller.handleRequest(request, response, service.patchChallenge);
};

const rejectChallenge = async (request, response) => {
  await Controller.handleRequest(request, response, service.rejectChallenge);
};

const starChallenge = async (request, response) => {
  await Controller.handleRequest(request, response, service.starChallenge);
};

const statisticsChallenge = async (request, response) => {
  await Controller.handleRequest(request, response, service.statisticsChallenge);
};


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
