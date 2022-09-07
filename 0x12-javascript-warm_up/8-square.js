#!/usr/bin/node

const { argv } = require('node:process');

const firstArg = parseInt(argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    let row = '';
    for (let j = 0; j < firstArg; j++) row += 'X';
    console.log(row);
  }
}
