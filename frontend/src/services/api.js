import axios from 'axios';

const API_URL = 'http://localhost:5000/api/items/items';

export const getAllItems = () => axios.get(API_URL);

export const createItem = (itemData) => axios.post(API_URL, itemData);

export const searchItems = (query) => axios.get(`${API_URL}?q=${query}`);

export const claimItem = (id) => axios.post(`${API_URL}/${id}/claim`);
