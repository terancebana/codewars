function narcissistic(value) {
  let strVal = value.toString().split('')
  let digit_size = strVal.length
  let sum = 0
  
  strVal.forEach(i =>{
    let val = parseInt(i)
    sum += Math.pow(val, digit_size)
  })
  
  return sum === value ? true : false
}
