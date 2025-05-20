function findSmallestInt(arr) {
  let smallest = arr[0]
  arr.forEach(i =>{
    if(i < smallest){
      smallest = i
    }
  })
  return smallest;
}