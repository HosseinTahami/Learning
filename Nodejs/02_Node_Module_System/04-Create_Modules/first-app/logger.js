var url = 'http://myloggr.io/log';


function log(message){


    // Send an Http Request
    console.log(message);
}


module.exports.log = log;
module.exports.endPoint = url;