var isSquare = function(n){
  if(n < 0){
    return false
  }else{
    let result = Math.sqrt(n)
    return result % 1 === 0
  }
}