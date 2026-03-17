//const path = require('path');

// const path = module.require('node:path');

const path = require('node:path');

//import {parse} from 'path';

var pathObj = path.parse(__filename);

console.log(pathObj);

