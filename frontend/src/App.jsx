import React, { useState, useEffect } from 'react';
import ItemForm from './components/ItemForm';
import ItemList from './components/ItemList';
import SearchBar from './components/SearchBar';
import { getAllItems, searchItems, claimItem } from './services/api';

function App() {
  const [items, setItems] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    loadItems();
  }, []);

  const loadItems = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await getAllItems();
      setItems(response.data);
    } catch (error) {
      setError('Failed to load items');
      console.error('Error loading items:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (value) => {
    setSearchTerm(value);
    setError('');
    if (value) {
      setLoading(true);
      try {
        const response = await searchItems(value);
        setItems(response.data);
      } catch (error) {
        setError('Error searching items');
        console.error('Error searching items:', error);
      } finally {
        setLoading(false);
      }
    } else {
      loadItems();
    }
  };

  const handleClaim = async (id) => {
    setError('');
    try {
      await claimItem(id);
      loadItems();
    } catch (error) {
      setError('Error claiming item');
      console.error('Error claiming item:', error);
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Lost and Found System</h1>

      <div className="mb-8">
        <h2 className="text-xl font-bold mb-4">Report Found Item</h2>
        <ItemForm onItemAdded={loadItems} />
      </div>

      <div className="mb-8">
        <h2 className="text-xl font-bold mb-4">Search Items</h2>
        <SearchBar searchTerm={searchTerm} onSearch={handleSearch} />
      </div>

      {error && <p className="text-red-500 mb-4">{error}</p>}
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ItemList items={items} onClaim={handleClaim} />
      )}
    </div>
  );
}

export default App;
