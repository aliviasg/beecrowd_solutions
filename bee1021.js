var x = parseFloat(lines.shift())

console.log("NOTAS:")
var a = x % 100
var r_a = (x - a) / 100
console.log(r_a+ " nota(s) de R$ 100.00")

var b = (a % 50)
var r_b = (a - b) / 50
console.log(r_b+ " nota(s) de R$ 50.00")

var c = (b % 20)
var r_c = (b - c) / 20
console.log(r_c+ " nota(s) de R$ 20.00")

var d = (c % 10)
var r_d = (c - d) / 10
console.log(r_d+ " nota(s) de R$ 10.00")

var e = (d % 5)
var r_e = (d - e) / 5
console.log(r_e+ " nota(s) de R$ 5.00")

var f = (e % 2)
var r_f = (e - f) / 2
console.log(r_f+ " nota(s) de R$ 2.00")

console.log("MOEDAS:")
var t = (f % 1)
var r_t = (f - t) / 1
console.log(r_t+ " moeda(s) de R$ 1.00")

var u = (t % 0.5)
var r_u = (t - u) / 0.5
console.log(r_u+ " moeda(s) de R$ 0.50")

var v = (u % 0.25)
var r_v = (u - v) / 0.25
console.log(r_v+ " moeda(s) de R$ 0.25")

var w = (v % 0.1)
var r_w = (v - w) / 0.1
console.log(r_w+ " moeda(s) de R$ 0.10")

var y = (w % 0.05)
var r_y = (w - y) / 0.05
console.log(r_y+ " moeda(s) de R$ 0.05")

var z = (y % 0.01)
var r_z = (y - z) / 0.01
console.log(r_z+ " moeda(s) de R$ 0.01")