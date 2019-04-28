class Complement
  def self.of_dna(string)
    string.tr('ATCG', 'UAGC')
  end
end
