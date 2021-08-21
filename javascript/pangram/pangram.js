export const isPangram = (string) => {
  const lettersUsed = {};
  for (let i = 0; i < string.length; i += 1) {
    const lowerCaseChar = string[i].toLowerCase();
    if (/[a-z]/.test(lowerCaseChar) && !lettersUsed[lowerCaseChar]) {
      lettersUsed[lowerCaseChar] = true;
    }
  }
  return Object.keys(lettersUsed).length === 26;
};
