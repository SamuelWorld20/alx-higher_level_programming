#!/usr/bin/node
const { argv } = require('process');
if (argv.slice(2).length === 0) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
