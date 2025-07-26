function spinWords(string) {
  let result = string.split(' ');
  for (let i = 0; i < result.length; i++) {
    if (result[i].length >= 5) {
      result[i] = result[i].split('').reverse().join('');
    }
  }
  return result.join(' ');
}
