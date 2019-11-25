import axios from 'axios';

export default () => axios.create({
  baseURL: 'http://52.47.46.54:5050',
  withCredentials: false,
  headers: {
    'Content-Type': 'multipart/form-data',
    'Access-Control-Allow-Origin': '*',
  },
});
