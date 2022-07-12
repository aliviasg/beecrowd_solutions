var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var answer = lines.shift();
var resp = answer.split(" ");
var [a,b,c] = resp;
a = parseFloat(a);
b = parseFloat(b);
c = parseFloat(c);
var delta = ((Math.pow(b,2)) - (4 * a * c));
var x1 = ((-b) + Math.sqrt(delta)) / (2 * a);
var x2 = ((-b) - Math.sqrt(delta)) / (2 * a);
 
if (isNaN(x1) || isNaN(x2) || a === 0) {console.log("Impossivel calcular")}
else {console.log("R1 = " + x1.toFixed(5));
console.log("R2 = " + x2.toFixed(5))}