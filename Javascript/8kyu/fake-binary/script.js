function fakeBin(x){
  return x.split('').map(val => {
    return val <  5 ? '0' : '1'
  }).join('')
}