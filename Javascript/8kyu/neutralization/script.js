function neutralise(s1, s2) {
  s1 = s1.split('')
  s2 = s2.split('')
  let result = []
  for(let i = 0; i < s1.length; i++){
    if(s1[i] === s2[i]){
      result.push(s1[i])
    }else{
      result.push('0')
    }
  }
  return result.join('');
}