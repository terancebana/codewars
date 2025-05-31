function XO(str) {
  let xCount = 0
  let oCount = 0
  str = str.toLowerCase().split('')
  for(let i = 0; i < str.length; i++){
    if(str[i] === 'x'){
      xCount++
    }else if(str[i] === 'o'){
      oCount++
    }
  }
  return xCount === oCount
}