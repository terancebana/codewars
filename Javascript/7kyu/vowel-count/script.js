function getCount(str) {
  
let newString = str.split('');
let count = 0;
  
  
for (let i = 0; i < newString.length; i++) {
	if (newString[i] === 'a' || newString[i] === 'e' || newString[i] === 'i' || newString[i] === 'o' || newString[i] === 'u') {
		count++;
	}

}
    return count;
}