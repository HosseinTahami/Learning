const EvenEmitter = require('events');

// var url = 'https://FuckLoggger.ai/log';



class Logger extends EvenEmitter {


    log(message) {

        // Send an HTTP Request
        console.log(message);

        // Raise an Event
        this.emit('messageLogged', {id:1, url:'https:fuck.com/log'});
    }
}




module.exports = Logger;