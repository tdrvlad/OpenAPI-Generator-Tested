/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Create a new evaluationPolicy.
*
* evaluationPolicy EvaluationPolicy The evaluationPolicy object to be created
* returns EvaluationPolicy
* */
const createEvaluationPolicy = ({ evaluationPolicy }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        evaluationPolicy,
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
* Retrieve list of evaluation policies
* Multiple status values can be provided with comma separated strings
*
* returns List
* */
const getEvaluationPolicyList = () => new Promise(
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

module.exports = {
  createEvaluationPolicy,
  getEvaluationPolicyList,
};
