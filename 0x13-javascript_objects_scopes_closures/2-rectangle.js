#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.rectangle = {};
    } else {
      this.rectangle = {
        width: w,
        height: h
      };
    }
  }
}

module.exports = Rectangle;
