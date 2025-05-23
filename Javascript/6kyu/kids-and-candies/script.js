function lcm(a, b) {
    return Math.abs(a * b) / gcd(a, b);
  }
  
  function gcd(a, b) {
    while (b) {
      let temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }
  
  let result = 1;
  for (let i = 1; i <= maxKids; i++) {
    result = lcm(result, i);
  }
  
  return result;