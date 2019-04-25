class Complement
  def self.of_dna(string)
    transformed = ""
    string.chars.each do |char|
      if char == "A"
        transformed << "U"
      elsif char == "T"
        transformed << "A"
      elsif char == "C"
        transformed << "G"
      elsif char == "G"
        transformed << "C"
      end
    end
    transformed
  end
end
