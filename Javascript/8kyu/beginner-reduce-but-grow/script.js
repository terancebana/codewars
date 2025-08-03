function grow(x){
  let result = 1
  x.forEach(val => result *= val)
  return result
}