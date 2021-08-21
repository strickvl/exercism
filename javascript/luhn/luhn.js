export const valid = (string) => {
  if (/[^0-9 ]/.test(string) || string.length <= 1 || !/[0-9]/.test(string[0])) return false;
  let vals = string.split("").map(char => {
    if (/[0-9]/.test(char)) {
      return Number(char);
    } else {
      return;
    }
  }).filter(val => val !== undefined);
  for (let i = vals.length - 2; i >= 0; i -= 2) {
    let value = vals[i];
    if (value * 2 > 9) {
      vals[i] = (value * 2) - 9;
    } else {
      vals[i] = value * 2;
    }
  }
  let sum = vals.reduce((acc, val) => {
    return acc + val;
  }, 0);

  if (sum % 10 === 0) {
    return true;
  } else {
    return false;
  }
};
