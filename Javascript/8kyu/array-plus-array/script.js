function arrayPlusArray(arr1, arr2) {
  let sum = 0
  arr1.forEach(i => sum += i)
  arr2.forEach(i => sum +=i)
  return sum
}