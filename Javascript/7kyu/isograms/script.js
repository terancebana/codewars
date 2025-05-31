function isIsogram(str){
  str = str.toLowerCase().split('').sort()
  let newStr = new Set(str)
  let arr = [...newStr].join('')
  
  str = str.join('')
  if(str === arr){
      return true
  }else{
      return false
  }
}