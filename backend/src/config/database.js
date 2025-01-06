const mongoose = require('mongoose');
const dotenv = require('dotenv');
dotenv.config();

/**
 * Asynchronously connects to the MongoDB database using the connection URI
 * specified in the environment variable `MONGODB_URI`.
 * 
 * @async
 * @function
 * @throws Will throw an error if the connection to the database fails.
 */
const connectDB = async () => {
    try {
        await mongoose.connect(process.env.MONGODB_URI); 
        console.log('Connected to the database successfully');
    } catch (error) {
        console.error('Error connecting to the database: ', error);
        process.exit(1);
    }
};

module.exports = connectDB;
