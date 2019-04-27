class Acronym
  def self.abbreviate(string)
    string_letters = string.chars.select {|char| char.match('[A-z ]')}.join("")
    abbrev = ""
    string_letters.split(" ").each do |word|
      abbrev << word[0].upcase
    end
    abbrev
  end
end
