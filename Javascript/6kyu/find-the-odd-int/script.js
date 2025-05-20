function findOdd(A) {
  for(let i = 0; i < A.length; i++){
    let appearances = 0
    for(let j = 0; j < A.length; j++){
      if(A[i] === A[j]){
        appearances++
      }
    }
    if(appearances % 2 != 0){
      return A[i]
    }else{
    }
  }
  return 0;
}