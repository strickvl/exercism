const SECONDS_IN_EARTH_YEAR = 31557600;

const planetYearsInEarthYears = {
  "earth": 1,
  "mercury": 0.2408467,
  "venus": 0.61519726,
  "mars": 1.8808158,
  "jupiter": 11.862615,
  "saturn": 29.447498,
  "uranus": 84.016846,
  "neptune": 164.79132,
}

const earthSecondsToYears = (seconds) => {
  return seconds / SECONDS_IN_EARTH_YEAR;
};

const parseAge = (age) => {
  return Number(age.toFixed(2));
}

export const age = (planet, seconds) => {
  const earthAge = earthSecondsToYears(seconds);
  return parseAge(earthAge / planetYearsInEarthYears[planet]);
};
