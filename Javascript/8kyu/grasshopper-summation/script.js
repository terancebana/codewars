var summation = function (num) {
  let sum = 0
  let start = 1
  if(num <= 1){
    return 1
  }else{
    for(let i = 1; i <= num; i++){
      sum += i
    }
  }
  return sum
}