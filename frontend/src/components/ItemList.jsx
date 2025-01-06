import React from 'react';
import ItemCard from './ItemCard';

const ItemList = ({ items, onClaim }) => (
  <div className="grid gap-4">
    {items.map((item) => (
      <ItemCard key={item._id} item={item} onClaim={onClaim} />
    ))}
  </div>
);

export default ItemList;
