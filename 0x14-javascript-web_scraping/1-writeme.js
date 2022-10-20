#!/usr/bin/node
const fs = require('fs');
file = process.argv[2]
str = process.argv[3]
fs.writeFile(file, str, 'utf8' (err) => {
	console.log(err);
});
