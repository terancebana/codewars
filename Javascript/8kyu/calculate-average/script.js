function findAverage(array) {
  let sum = 0;
  if (!array || array.length === 0) {
    return 0;
  } else {
    array.forEach((i) => {
      sum += i;
    });
    return sum / array.length;
  }
}