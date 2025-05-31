function makeSentence(parts) {
    for (let i = 0; i < parts.length; i++) {
        if (parts[i] === ',') {
            parts[i - 1] += parts[i];
            parts.splice(i, 1);
            i--;
        } else if (parts[i] === '.') {
            parts.splice(i, 1);
            i--;
        }
    }

    let result = parts.join(' ');

    if (!result.endsWith('.')) {
        result += '.';
    }

    return result;
}

console.log(makeSentence(['hello', ',', 'my', 'dear', '.', '.']));