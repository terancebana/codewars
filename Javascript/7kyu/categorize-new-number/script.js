function openOrSenior(data){
  let result = []
  for(let i = 0; i < data.length; i++){
    let member = data[i]
    if(member[0] >= 55 && member[1] > 7){
      result.push('Senior')
    }else{
      result.push('Open')
    }
  }
  return result
}