function digitize(n) {
  let str = n.toString()
  str = str.split("").reverse()
  let numArr = []
  str.forEach(i => {
    numArr.push(parseInt(i))
  })
  return numArr
}