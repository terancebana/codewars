function highAndLow(numbers){
  numbers = numbers.split(" ")
  let max = Math.max(...numbers).toString()
  let min = Math.min(...numbers).toString()
  
  return `${max} ${min}`
}