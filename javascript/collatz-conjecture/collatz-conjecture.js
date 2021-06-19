export const steps = (n) => {
  if (n < 1) throw "Only positive numbers are allowed";
  let steps = 0;
  if (n === 1) return steps;

  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
    } else {
      n = (n * 3) + 1;
    }
    steps += 1;
  }

  return steps;
};
