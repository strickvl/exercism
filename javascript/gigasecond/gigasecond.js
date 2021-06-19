export const gigasecond = (date) => {
  const GIGASECOND = 1000000000;
  const MILLISECONDS = 1000;
  let secsSinceEpoch = date.getTime(date);
  let newTime = secsSinceEpoch + (GIGASECOND * MILLISECONDS);
  return new Date(newTime);
};
