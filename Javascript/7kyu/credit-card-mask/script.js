function maskify(cc) {
  if (!cc || cc.length <= 4) {
    return cc;
  } else {
    let new_cc = cc.split('');
    let lastFour = new_cc.slice(-4).join('');
    let masked = new_cc.slice(0, -4).join('').replace(/./g, '#');
    return masked + lastFour;
  }
}