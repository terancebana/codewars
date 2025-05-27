function basicOp(operation, value1, value2){
  operation = operation.toString()
  switch(operation){
      case "+":
      return value1 + value2
      break
      
      case "-":
      return value1 - value2
      break
      
      case "*":
      return value1 * value2
      break
      
      case "/":
      return value1/value2
      break
      
      default:
      return "Enter a valid operation or number"
      break
  }
}