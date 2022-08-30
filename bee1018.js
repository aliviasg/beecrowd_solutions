//Cédulas

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var x = parseInt(lines.shift())
console.log(x)

var a = x % 100
var r_a = (x - a) / 100
console.log(r_a+ " nota(s) de R$ 100,00")

var b = (a % 50)
var r_b = (a - b) / 50
console.log(r_b+ " nota(s) de R$ 50,00")

var c = (b % 20)
var r_c = (b - c) / 20
console.log(r_c+ " nota(s) de R$ 20,00")

var d = (c % 10)
var r_d = (c - d) / 10
console.log(r_d+ " nota(s) de R$ 10,00")

var e = (d % 5)
var r_e = (d - e) / 5
console.log(r_e+ " nota(s) de R$ 5,00")

var f = (e % 2)
var r_f = (e - f) / 2
console.log(r_f+ " nota(s) de R$ 2,00")

var g = (f % 1)
var r_g = (f - g) / 1
console.log(r_g+ " nota(s) de R$ 1,00")
