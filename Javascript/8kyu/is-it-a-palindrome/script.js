function isPalindrome(x) {
  let new_x = x.toLowerCase()
  let reverseStr = new_x.split('').reverse().join('')
  return new_x === reverseStr ? true : false
}