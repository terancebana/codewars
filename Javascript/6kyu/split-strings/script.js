function solution(str){
  if(str){
    let result = str.match(/.{1,2}/g);
    if(str.length % 2 != 0){
        result[result.length - 1] = result[result.length - 1] + "_"
    }
    return result
  }else{
    return []
  }
}