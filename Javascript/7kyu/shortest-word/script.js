function findShort(s){
  let s_arr = s.split(' ')
  let result = []
  for(let i = 0; i < s_arr.length; i++){
     result.push(s_arr[i].length) 
  }
  return Math.min(...result)
}