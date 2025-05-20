function countSheeps(sheep) {
  let present = 0
  sheep.forEach(i =>{
    if(i === true){
      present++
    }
  })
  return present
}