#!/usr/bin/node
const { argv } = require('process');
console.log(argv.slice(2).length);
if (argv.slice(2).length === 0) {
  console.log('No argument');
} else if (argv.slice(2).length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
