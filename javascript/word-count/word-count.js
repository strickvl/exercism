export const countWords = (string) => {
  let cleanStr = string.replaceAll(/\s/g, ' ');
  cleanStr = cleanStr.replaceAll(/[^a-zA-Z1-9\']/g, " ");
  let arr = cleanStr.split(/\s+/);
  arr = arr.map(word => {
    return word.toLowerCase().replaceAll(/^\'|\'$/g, "")
  });
  let counts = {};
  arr = arr.filter(word => word !== '');
  arr.forEach(word => {
    if (!counts[word]) {
      counts[word] = 1;
    } else {
      counts[word] += 1;
    }
  });
  return counts;
};
