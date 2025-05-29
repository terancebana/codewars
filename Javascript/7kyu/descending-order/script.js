function descendingOrder(n){
  n = n.toString().split('').sort()
  return parseInt(n.reverse().join(''))
}