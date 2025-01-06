import React from 'react';

const ItemCard = ({ item, onClaim }) => (
  <div className="border rounded p-4">
    <h3 className="font-bold">{item.itemType}</h3>
    <p>Name: {item.name}</p>
    <p>Location: {item.location}</p>
    <p>Date Found: {new Date(item.dateFound).toLocaleDateString()}</p>
    <p>Status: {item.status}</p>
    {item.status === 'unclaimed' && (
      <button
        onClick={() => onClaim(item._id)}
        className="bg-green-500 text-white px-4 py-2 rounded mt-2"
      >
        Claim Item
      </button>
    )}
  </div>
);

export default ItemCard;