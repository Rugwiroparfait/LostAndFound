import React from 'react';

const SearchBar = ({ searchTerm, onSearch }) => (
  <input
    type="text"
    placeholder="Search by name..."
    value={searchTerm}
    onChange={(e) => onSearch(e.target.value)}
    className="w-full p-2 border rounded mb-4"
  />
);

export default SearchBar;