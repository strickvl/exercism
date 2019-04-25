class ResistorColorDuo
  COLOUR_VALS = {
    "black" => 0,
    "brown" => 1,
    "red" => 2,
    "orange" => 3,
    "yellow" => 4,
    "green" => 5,
    "blue" => 6,
    "violet" => 7,
    "grey" => 8,
    "white" => 9
  }
  def self.value(arr)
    first_val = COLOUR_VALS[arr[0]]
    second_val = COLOUR_VALS[arr[1]]
    "#{first_val}#{second_val}".to_i
  end
end
