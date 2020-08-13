/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Delete mediaItem
* Multiple status values can be provided with comma separated strings
*
* string List The challenge object to be created
* no response value expected for this operation
* */
const deleteMediaItems = ({ string }) => new Promise(
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
* Retrieve media item
* Multiple status values can be provided with comma separated strings
*
* bucketName String bucket name
* mediaItem String media item
* returns byte[]
* */
const getMediaItem = ({ bucketName, mediaItem }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        bucketName,
        mediaItem,
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
* Retrieve list of mediaItems
* Multiple status values can be provided with comma separated strings
*
* datasetId String 
* pageSize Integer  (optional)
* pageNumber Integer  (optional)
* returns List
* */
const getMediaItemList = ({ datasetId, pageSize, pageNumber }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        datasetId,
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

module.exports = {
  deleteMediaItems,
  getMediaItem,
  getMediaItemList,
};
