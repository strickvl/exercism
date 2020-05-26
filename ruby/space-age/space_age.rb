class SpaceAge
  EARTH_ORBITAL_PERIOD_IN_SECONDS = 31557600

  def initialize(seconds)
    @age_in_seconds = seconds
  end

  def on_earth
    (@age_in_seconds.to_f / EARTH_ORBITAL_PERIOD_IN_SECONDS).round(2)
  end

  def on_mercury
    (@age_in_seconds.to_f / (EARTH_ORBITAL_PERIOD_IN_SECONDS * 0.2408467)).round(2)
  end

  def on_venus
    (@age_in_seconds.to_f / (EARTH_ORBITAL_PERIOD_IN_SECONDS * 0.61519726)).round(2)
  end

  def on_mars
    (@age_in_seconds.to_f / (EARTH_ORBITAL_PERIOD_IN_SECONDS * 1.8808158)).round(2)
  end

  def on_jupiter
    (@age_in_seconds.to_f / (EARTH_ORBITAL_PERIOD_IN_SECONDS * 11.862615)).round(2)
  end

  def on_saturn
    (@age_in_seconds.to_f / (EARTH_ORBITAL_PERIOD_IN_SECONDS * 29.447498)).round(2)
  end

  def on_uranus
    (@age_in_seconds.to_f / (EARTH_ORBITAL_PERIOD_IN_SECONDS * 84.016846)).round(2)
  end

  def on_neptune
    (@age_in_seconds.to_f / (EARTH_ORBITAL_PERIOD_IN_SECONDS * 164.79132)).round(2)
  end
end
