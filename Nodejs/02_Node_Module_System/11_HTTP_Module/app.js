const http = require('http');

// const server = http.createServer();

// // Register a Listener
// server.on('connection', (socket) => {
//     console.log('New Connection...');
// })

const server = http.createServer((req, res)=>{

    if (req.url == '/'){
        res.write('<h1>Hello, World</h1>');
        res.end();
    }

});

// Start the fucking Engine
server.listen(3000);

console.log('Listening on Port 30000');