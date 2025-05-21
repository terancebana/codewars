function incrementString(strng) {
  let pattern = /(\d*)$/;
  let [fullMatch, nberPart] = strng.match(pattern) || ['', ''];
  let strPart = strng.slice(0, strng.length - fullMatch.length);
  
  if(nberPart === '') {
    return strng + '1';
  } else {
    let number = parseInt(nberPart) + 1;
    let paddedNumber = number.toString().padStart(nberPart.length, '0');
    return strPart + paddedNumber;
  }
}