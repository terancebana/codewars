function splitAndAdd(arr, n) {
  let middle = Math.floor((arr.length/2))
  let upperArr = [], lowerArr = []
  
  splitArr(arr, middle, upperArr, lowerArr)
  
  Add(upperArr, lowerArr)
}




function splitArr(arr,middle, upperArr, lowerArr){
    for(let i = 0; i < arr.length; i++){
    if(i < middle){
      upperArr.push(arr[i])
    }else{
      lowerArr.push(arr[i])
    }
  }
//   console.log(upperArr, lowerArr)
}


function Add(upperArr, lowerArr){
    let shorterArr = upperArr.length > lowerArr.length ? "LowerArr" : "UpperArr"
    console.log(shorterArr)
    let result = []
    let arrDiff = Math.abs(upperArr.length - lowerArr.length)
    

}



splitAndAdd([3, 2, 4, 5, 6, 7], 2)