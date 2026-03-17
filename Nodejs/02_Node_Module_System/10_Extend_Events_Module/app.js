const EvenEmitter = require('events');



const Logger = require('./logger');
const logger = new Logger();

// Register Listener
logger.on('messageLogged', (arg)=>{
    console.log('Listener Called',arg);
});

logger.log('message');