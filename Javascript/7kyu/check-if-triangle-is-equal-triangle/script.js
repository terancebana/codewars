function equableTriangle(a,b,c) {
  let perimeter = a + b + c
  let semiPerim = perimeter/2
  let area = Math.sqrt(semiPerim * (semiPerim - a) * (semiPerim - b) * (semiPerim - c))
  
  return area === perimeter
}