function twoSum(numbers, target) {
  let result = []
  for(let i = 0; i < numbers.length; i++){
    for(let j = 0; j < numbers.length; j++){
      if( i === j){
        continue
      }else{
        if( numbers[i] + numbers[j] === target){
          result = [i, j]
        }
      }
    }
  }
    return result;
}