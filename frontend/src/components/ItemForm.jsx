import React, { useState } from 'react';
import { createItem } from '../services/api';

const ItemForm = ({ onItemAdded }) => {
  const [formData, setFormData] = useState({
    itemType: '',
    name: '',
    location: '',
    dateFound: '',
    description: '',
    contactInfo: '',
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const result = await createItem(formData);
      onItemAdded(result.data);
      setFormData({
        itemType: '',
        name: '',
        location: '',
        dateFound: '',
        description: '',
        contactInfo: '',
      });
    } catch (error) {
      console.error('Error adding item:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 p-4 bg-white shadow-md rounded">
      {/* Form Fields */}
      <button type="submit" className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
        Submit Found Item
      </button>
    </form>
  );
};

export default ItemForm;
