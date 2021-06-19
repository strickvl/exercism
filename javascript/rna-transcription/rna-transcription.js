const mapLetter = (char) => {
  if (char === "C") {
    return "G";
  } else if (char === "G") {
    return "C";
  } else if (char === "T") {
    return "A";
  } else if (char === "A") {
    return "U";
  }
};

export const toRna = (str) => {
  return str.split('').map(char => mapLetter(char)).join('');
};
