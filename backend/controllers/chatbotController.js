const chatbotModel = require('../models/chatbotModel');

exports.ask = async (req, res) => {
    try {
        const question = req.body.question;
        console.log(`Received question: ${question}`);
        const answer = await chatbotModel.getAnswer(question);
        console.log(`Response from model: ${answer}`);
        res.json({ answer: answer || 'I didn\'t understand that.' });
    } catch (error) {
        console.error('Error in controller:', error);
        res.status(500).json({ error: 'An error occurred' });
    }
};
