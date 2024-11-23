const express = require('express');
const router = express.Router();
const chatbotController = require('../controllers/chatbotController');

// POST request to handle chatbot interaction
router.post('/ask', chatbotController.ask);

module.exports = router;
