const EventEmitter = require('events')
//import EvenEmitter from 'events'
const emitter = new EventEmitter();

// Register Listener
emitter.on('messageLogged', (arg)=>{
    
    console.log('Listener Called.');
    console.log(arg);
    }
)


// Making a noise, Creating a signal
event_argument = {
    id: 1,
    url: 'https://FuckYou.org'
}

emitter.emit('messageLogged', event_argument)