#!/usr/bin/node
console.log(process.argv);
if (process.argv === 0) {
  console.log('No argument');
} else if (process.argv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
