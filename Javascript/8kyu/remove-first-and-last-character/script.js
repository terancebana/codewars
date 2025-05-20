function removeChar(str){
    let newstr = str.split('');
    newstr.shift();
    newstr.pop();
    return newstr.join('');
};