/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* add media items to dataset
* Multiple status values can be provided with comma separated strings
*
* datasetId String 
* no response value expected for this operation
* */
const addMediaItem = ({ datasetId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        datasetId,
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
* Retrieve list of datasets
* Multiple status values can be provided with comma separated strings
*
* datasetName String  (optional)
* datasetType String  (optional)
* staticImage String  (optional)
* returns Dataset
* */
const createDataset = ({ datasetName, datasetType, staticImage }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        datasetName,
        datasetType,
        staticImage,
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
* Delete dataset
* Multiple status values can be provided with comma separated strings
*
* string List The challenge object to be created
* no response value expected for this operation
* */
const deleteDataset = ({ string }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        string,
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
* Retrieve dataset info
* Multiple status values can be provided with comma separated strings
*
* datasetId String The identifier of the dataset
* returns Dataset
* */
const getDataset = ({ datasetId }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        datasetId,
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
* Retrieve list of datasets
* Multiple status values can be provided with comma separated strings
*
* returns List
* */
const getDatasetList = () => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
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
* Retrieve list of static images
* Multiple status values can be provided with comma separated strings
*
* returns List
* */
const getDatasetStaticImages = () => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
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
* get estimated cost for storage
* optional parameter datasetId for new shards
*
* datasetId String  (optional)
* size Double  (optional)
* returns DatasetStorageCost
* */
const getStorageCost = ({ datasetId, size }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        datasetId,
        size,
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
  addMediaItem,
  createDataset,
  deleteDataset,
  getDataset,
  getDatasetList,
  getDatasetStaticImages,
  getStorageCost,
};
