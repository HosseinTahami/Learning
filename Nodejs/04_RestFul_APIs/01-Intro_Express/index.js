const express = require('express')
const app = express();



app.get('/', (req, res)=>{

    res.send('<h1>Hello World</h1>');
});

app.get('/api/courses', (req, res) => {
    res.send([1, 4, 5, 23, 5, 43, 2331, 43, 12]);
})


app.get('/api/courses/:id/:year/:month', (req, res)=>{
    res.send(req.query);
})



// PORT 

const port = process.env.PORT || 3000 // export PORT=5000 in terminal

app.listen(port, ()=> console.log(`Listening on port ${port}...`));
