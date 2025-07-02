function sortByArea(array) {
  let areas = {}
  let result = []
  for(let i = 0; i < array.length; i++){
    if(typeof(array[i]) === 'object'){
      areas[array[i].toString()] = array[i][0] * array[i][1]
    }else{
      areas[array[i].toString()] = 3.14 *(Math.pow(array[i], 2))
    }
  }
  
  let areasArr = Object.entries(areas)
  areasArr.sort((a, b) => a[1] - b[1])
  
  for(let i = 0; i < areasArr.length; i ++){
      let value = areasArr[i][0].split(',');
      if (value.length == 1) {
          value = parseFloat(value[0]);
          result.push(value);
      } else {
          let ref_arr = [];
          for(let j=0; j < value.length; j++) {
            ref_arr.push(parseFloat(value[j]));
          }
          result.push(ref_arr);
      }
  }
  return result
}



