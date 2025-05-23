function candiesToBuy( kids ){
  
  function gcd(a, b) {
    while (b) {
      let temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }
  function lcm(a, b) {
      return (a * b) / gcd(a, b);
    }

    let minCandies = 1;
    for (let i = 1; i <= kids; i++) {
      minCandies = lcm(minCandies, i);
    }

    return minCandies;
}
