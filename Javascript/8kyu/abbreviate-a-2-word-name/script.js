function abbrevName(name){
  name = name.toString().split(" ")
  
  let Fname = name[0].toUpperCase()
  let Lname = name[1].toUpperCase()
  
  return `${Fname[0]}.${Lname[0]}`
}