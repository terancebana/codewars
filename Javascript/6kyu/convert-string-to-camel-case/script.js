function toCamelCase(str){
  if(str){
    str = str.split('')
    let result = []
    for(let i = 0; i < str.length; i++){
        if(str[i] === '-' || str[i] === '_'){
            str[i+1] = str[i+1].toUpperCase()
            result = str.splice(i, 1)
        }
    }
    return str.join('')
  }else{
      return ""
  }
}