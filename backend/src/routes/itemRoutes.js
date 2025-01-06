const express = require('express');
const router = express.Router();
const itemController = require('../controllers/itemController');

router.post('/items', itemController.createItem);
router.get('/items', itemController.getallItems);
router.get('/items/search', itemController.searchItems);
router.put('/items/:id/claim', itemController.claimItem);

module.exports = router;