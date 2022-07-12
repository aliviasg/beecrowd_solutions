var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var answer = lines.shift()
var resp = answer.split(" ");
  var [x,y] = resp
  x = parseInt(x)
  y = parseInt(y)
  var total

 if (x === y) {
   console.log("O JOGO DUROU 24 HORA(S)")
 } else {
   if (y < x) {
     total = (24 - x) + y
   } else {
     total = y - x
   } console.log("O JOGO DUROU " +total+ " HORA(S)")
 }