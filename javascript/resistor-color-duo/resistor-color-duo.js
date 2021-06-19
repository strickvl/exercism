export const colorCode = (code) => {
  return COLORS.indexOf(code);
};

export const decodedValue = (colours) => {
  let num = 0;

  for (let i = 0; i < 2; i += 1) {
    if (i === 0) {
      num += colorCode(colours[i]) * 10;
    } else {
      num += colorCode(colours[i]);
    }
  }

  return num;
};

const COLORS = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white',
];
