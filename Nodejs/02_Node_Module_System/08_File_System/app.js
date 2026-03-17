const fs = require('fs');

files = fs.readdirSync('./../');
console.log(files);


fs.readdir('./../', 
            (err, files) => {
                if (err) console.log("Error");
                else console.log(files);   
            }
)
