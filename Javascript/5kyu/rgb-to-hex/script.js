function rgb(r, g, b) {
  const rangeR = Math.min(255, Math.max(0, r));
  const rangeG = Math.min(255, Math.max(0, g));
  const rangeB = Math.min(255, Math.max(0, b));
  
  const hexR = rangeR.toString(16).padStart(2, '0')
  const hexG = rangeG.toString(16).padStart(2, '0')
  const hexB = rangeB.toString(16).padStart(2, '0')
  return (hexR + hexG + hexB).toUpperCase();
}