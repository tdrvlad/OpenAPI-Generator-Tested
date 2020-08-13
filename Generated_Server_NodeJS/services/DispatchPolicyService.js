/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Create a new dispatchPolicy.
*
* dispatchPolicy DispatchPolicy The dispatchPolicy object to be created
* returns DispatchPolicy
* */
const createDispatchPolicy = ({ dispatchPolicy }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        dispatchPolicy,
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
* Retrieve list of dispatch policies
* Multiple status values can be provided with comma separated strings
*
* returns List
* */
const getDispatchPolicyList = () => new Promise(
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
  createDispatchPolicy,
  getDispatchPolicyList,
};
