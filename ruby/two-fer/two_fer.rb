class TwoFer
  def self.two_fer(name = "")
    return "One for you, one for me." if name == ""
    return "One for #{name}, one for me."
  end
end
