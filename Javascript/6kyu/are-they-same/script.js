function comp(array1, array2){
  let isPresentArr = []
  let isPresent = false
  let isUsed = []
  if(array1 === null || array2 === null){
    return false
  }else if(array1.length != array2.length){
    return false
  }else{
    for(let i = 0; i < array1.length; i++){
      for(let j = 0; j < array2.length; j++){
        if(array1[i] === Math.sqrt(array2[j]) && isUsed.includes(j) === false){
          isUsed.push(j)
          isPresentArr.push(true)
          isPresent = true
          break
        }
      }
      if(isPresent === false){
        return false
      }
      isPresent = false
    }
    for(let i = 0; i < isPresentArr.length; i++){
      if(isPresentArr[i] === false){
        return false
      }
    }
    return true
  }
}

