function hello(name) {
  if(name === '' || !name){
    return 'Hello, World!'
  }else{
    name = name.toLowerCase().split('')
    name[0] = name[0].toUpperCase()
    return `Hello, ${name.join('')}!`
  }
  return ;
}