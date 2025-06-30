function flickSwitch(arr){
  let results = [], boolean = true
  arr.forEach(i => {
    if(i === 'flick'){
      boolean = !boolean
      results.push(boolean)
    }else{
      results.push(boolean)
    }
  })
  return results ;
}