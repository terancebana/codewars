function longest(s1, s2) {
  s1 = s1.split(''), s2 = s2.split('')
  s1.push(...s2)
  let mergeSet = new Set(s1)
  let result = [...mergeSet]
  return result.sort().join('')
}