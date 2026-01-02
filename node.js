const express = require('express');
const path = require('path');
const app = express();

app.use(express.static('public'));
app.use(express.json());

app.post('/webhook', (req, res) => {
    console.log('Data from Mini App:', req.body);
    res.json({ status: 'received' });
});

app.listen(3000, () => {
    console.log('Server running on https://localhost:3000');
});