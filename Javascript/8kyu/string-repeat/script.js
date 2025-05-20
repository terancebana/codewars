function repeatStr (n, s) {
  if(n < 0){
    return "Use valid number or string"
  }else{
    return s.repeat(n)
  }
  return '';
}

console.log(repeatStr(3, 'hello')); // hellohellohello