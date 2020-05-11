class Pangram
  def self.pangram?(string)
    string_chars = string.downcase.chars.select do |char|
      char.match(/[a-z]/)
    end.uniq
    string_chars.size == 26 ? true : false
  end
end
