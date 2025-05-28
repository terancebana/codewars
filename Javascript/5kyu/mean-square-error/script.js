const solution = function(firstArray, secondArray) {
  let diffArr = []
  let sum = 0
  for (let i = 0; i < firstArray.length; i++){
    diffArr.push(Math.pow(Math.abs(secondArray[i] - firstArray[i]), 2))
  }
  
  diffArr.forEach(i => {
    sum+= i
  })
  
  return sum/firstArray.length
}