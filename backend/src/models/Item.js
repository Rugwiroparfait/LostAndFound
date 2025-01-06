const mongoose = require('mongoose');

const itemSchema = new mongoose.Schema({
    ItemType: {
        type: String,
        required: true,
        enum: ['Passport', 'ID Card', 'Driver License', 'Others']
    },
    name: {
        type: String,
        required: true
    },
    location: {
        type: String,
        required: true
    },
    dateFound: {
        type: Date,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    contact: {
        type: String,
        required: true
    },
    status: {
        type: String,
        required: true,
        enum: ['Found', 'Claimed']
    }
});

module.exports = mongoose.model('Item', itemSchema);