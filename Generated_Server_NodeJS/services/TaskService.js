/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Get new task
* Multiple status values can be provided with comma separated strings
*
* challengeId String The identifier of the challenge
* returns GetTaskResponse
* */
const getTask = ({ challengeId }) => new Promise(
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
* Submit  task
* Multiple status values can be provided with comma separated strings
*
* taskId String The identifier of the challenge
* task Task task object
* returns Task
* */
const submitTask = ({ taskId, task }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        taskId,
        task,
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
  getTask,
  submitTask,
};
