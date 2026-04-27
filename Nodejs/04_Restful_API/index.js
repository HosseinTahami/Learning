// import express from 'express';
const express = require('express');

const app = express();

app.use(express.json());

app.get('/', (req, res) =>{

    res.send("Hello Fuckers");

});


app.get('/api/courses', (req, res) => {
    res.send([1, 4, 5]);
});


app.get('/api/courses/:id', (req, res) =>{
    res.send(req.params.id);
});

app.get('/api/posts/:year/:month', (req, res) => {
    // res.send(req.params);

    // /api/posts/2018/3/?sortBy=name
    // {sortBy : "name"}
    res.send(req.query);
});


books = [
    {id: 1, name: "Robin", author: "Fucker"},
    {id: 2, name: "Rodin", author: "Fucker2"},
    {id: 3, name: "Robindd", author: "Fucker3"},
]

app.get('/api/books/:id', (req, res) => {

    const book = books.find( book => book.id === parseInt(req.params.id) )

    if (!book){
        res.status(404).send("bro too koonam")
    }
    res.send(book)
});

app.post('/api/books/', (req, res) => {

    const book = {
        id: books.length + 1,
        name: req.body.name
    }

    books.push(book);
    res.send(book);
});

// export PORT=5000 --.=> in terminal
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Listening on port ${port}...`))