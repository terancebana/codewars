function squareDigits(num){
  let str = num.toString()
  str  = str.split("")
  for(let i = 0; i < str.length; i++){
    str[i] = Math.pow(parseInt(str[i]), 2)
  }
  
  return parseInt(str.join(""));
}