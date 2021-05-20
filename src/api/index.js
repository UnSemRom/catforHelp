import axios from 'axios';

//const baseURL = 'http://167.86.73.208:5005'
const baseURL = 'http://127.0.0.1:5000'

export {
  baseURL
};

const $http = axios.create({
  baseURL,
});

export default $http;