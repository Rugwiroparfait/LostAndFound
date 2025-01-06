const Item = require('../models/Item');

// create a new item

exports.createItem = async (req, res) => {
    try {
        /**
         * Creates a new item in the database.
         *
         * @param {Object} req - The request object.
         * @param {Object} req.body - The body of the request containing item details.
         * @returns {Promise<Object>} The newly created item.
         * @throws {Error} If there is an error during item creation.
         */
        const newItem = await Item.create(req.body);
        await newItem.save();
        res.status(201).json(newItem);
    } catch (error) {
        res.status(400).json({ message: error });
    }
};

// get all items
exports.getallItems = async (req, res) => {
    try {
        /**
         * Retrieves all items from the database, sorted by creation date in descending order.
         *
         * @returns {Promise<Array>} A promise that resolves to an array of items.
         */
        const items = await Item.find().sort({ createdAt: -1 });
        res.status(200).json(items);
    }
    catch (error) {
        res.status(400).json({ message: error });
    }
};



// search for an item by name

exports.searchItems = async (req, res) => {
    try {
        const { name } = req.query;

        // Check if the name query parameter is provided
        if (!name) {
            return res.status(400).json({ message: 'Query parameter "name" is required' });
        }

        /**
         * Retrieves items from the database that match the given name pattern.
         *
         * @param {string} name - The name pattern to search for, using a case-insensitive regular expression.
         * @returns {Promise<Array>} - A promise that resolves to an array of items that match the search criteria.
         * @throws {Error} - Throws an error if the database query fails.
         */
        const items = await Item.find({
            name: { $regex: name, $options: 'i' }
        });

        res.status(200).json(items);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// claim an item

exports.claimItem = async (req, res) => {
    try {
        /**
         * Retrieves an item by its ID.
         *
         * @param {Object} req - The request object.
         * @param {Object} req.params - The parameters of the request.
         * @param {string} req.params.id - The ID of the item to retrieve.
         * @returns {Promise<Object>} The item object if found.
         * @throws {Error} If the item is not found or there is a database error.
         */
        const item = await Item.findById(req.params.id);
        if (!item) {
            return res.status(404).json({ message: 'Item not found' });
        }
        item.status = 'Claimed';
        await item.save();
        res.json(item);
    } catch (error) {
        res.status(500).json({ message: error });
    }
};