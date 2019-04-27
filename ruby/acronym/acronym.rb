class Acronym
  def self.abbreviate(string)
    clean_string = string.gsub(" - ", "-")
    abbrev = string.chars.first.upcase
    clean_string.chars.each_with_index do |char, idx|
      abbrev << clean_string[idx+1].upcase if char == " " || char == "-"
    end
    abbrev
  end
end
