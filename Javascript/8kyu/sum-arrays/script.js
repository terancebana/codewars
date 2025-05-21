function sum (numbers) {
  let sum = 0
  if(numbers === null){
    return 0
  }else{
    numbers.forEach(i =>{
      sum+=i
    })
  }
  return sum
}