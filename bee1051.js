var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
 
 var answer = lines.shift()
 
  var x = parseFloat(answer)

  if (x <= 2000.00) {
   console.log("Isento")
 } else {
    var y = x - 2000.00
    y = y > 0 ? y : 0

    var z = x - 3000.00
    z = z > 0 ? z : 0

    var w = x - 4500.00
    w = w > 0 ? w : 0
    
    var imposto_y = (8/100) * (y - z)
    var imposto_z = (18/100) * (z - w)
    var imposto_w = (28/100) * w 

    var total = imposto_y + imposto_z + imposto_w
    console.log("R$ " + total.toFixed(2))
  }
