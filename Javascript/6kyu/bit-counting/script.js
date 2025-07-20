function countBits(n) {
    let num = n.toString(2).split('')
    let result = num.filter(i => i == 1)
    return result.length
}
