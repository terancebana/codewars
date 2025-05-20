function count(string) {
  let result = {}
  let occurence = 0
  let newStr  = string.split("")
  let uniqueArr = [...new Set(newStr)];
  for(let i = 0; i < uniqueArr.length; i++){
    for(let j = 0; j < newStr.length; j++){
      if(uniqueArr[i] === newStr[j]){
        occurence++
      }
    }
    result[uniqueArr[i]] = occurence
    occurence = 0
  }
  return result;
}