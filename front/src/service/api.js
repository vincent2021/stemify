import axios from 'axios';

export default () => axios.create({
  baseURL: 'http://15.188.47.18:5050',
  withCredentials: false,
  headers: {
    'Content-Type': 'multipart/form-data',
    'Access-Control-Allow-Origin': '*',
  },
});
