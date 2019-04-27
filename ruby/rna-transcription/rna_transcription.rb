class Complement
  DNA_TO_RNA = {
    "A" => "U",
    "T" => "A",
    "C" => "G",
    "G" => "C"
  }
  def self.of_dna(string)
    string.chars.map do |char|
      DNA_TO_RNA[char]
    end.join("")
  end
end
