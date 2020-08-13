/**
 * The DatasetController file is a very simple one, which does not need to be changed manually,
 * unless there's a case where business logic reoutes the request to an entity which is not
 * the service.
 * The heavy lifting of the Controller item is done in Request.js - that is where request
 * parameters are extracted and sent to the service, and where response is handled.
 */

const Controller = require('./Controller');
const service = require('../services/DatasetService');
const addMediaItem = async (request, response) => {
  await Controller.handleRequest(request, response, service.addMediaItem);
};

const createDataset = async (request, response) => {
  await Controller.handleRequest(request, response, service.createDataset);
};

const deleteDataset = async (request, response) => {
  await Controller.handleRequest(request, response, service.deleteDataset);
};

const getDataset = async (request, response) => {
  await Controller.handleRequest(request, response, service.getDataset);
};

const getDatasetList = async (request, response) => {
  await Controller.handleRequest(request, response, service.getDatasetList);
};

const getDatasetStaticImages = async (request, response) => {
  await Controller.handleRequest(request, response, service.getDatasetStaticImages);
};

const getStorageCost = async (request, response) => {
  await Controller.handleRequest(request, response, service.getStorageCost);
};


module.exports = {
  addMediaItem,
  createDataset,
  deleteDataset,
  getDataset,
  getDatasetList,
  getDatasetStaticImages,
  getStorageCost,
};
