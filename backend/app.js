const express = require('express');
const path = require('path');
const app = express();

// Middleware
app.use(express.json());

// Serve static files from the frontend directory
app.use(express.static(path.join(__dirname, '../frontend')));

// routes
app.use('/api/chatbot', require('./routes/chatbot'));

// other routes by serving the index.html file
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/index.html'));
});

// server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log("now app is listning");
})
// app.listen(PORT, () => console.log(`Server is running on http://localhost:${PORT}`));
