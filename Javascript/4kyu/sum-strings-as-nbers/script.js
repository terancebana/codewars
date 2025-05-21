function sumStrings(a,b) {
  if(a === "" && b !== ""){
    return b
  }else if(a !== "" && b === ""){
    return a
  }else{
    let newA = BigInt(a)
    let newB = BigInt(b)
    let sum = newA + newB
    return sum.toString()
  }
}