function lamps(a) {
  let comp_a = [], comp_b = [], changes_a = 0, changes_b = 0
  
  for(let i = 0; i < a.length; i++){
      if( i % 2 == 0){
          comp_a.push(1)
          comp_b.push(0)
      }else{
          comp_a.push(0)
          comp_b.push(1)
      }
  }

//   console.log(comp_a)
//   console.log(comp_b)
  
 for(let i = 0; i < a.length; i++){
     if( a[i] !== comp_a[i]){
         changes_a++
     }else if( a[i] !== comp_b[i]){
         changes_b++
     }
 }
 
 return changes_a > changes_b ? changes_b : changes_a
  

}

console.log(lamps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))