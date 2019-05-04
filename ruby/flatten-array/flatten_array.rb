class FlattenArray
  def self.flatten(arr)
    arr = arr.compact
    final = []
    arr.each do |item|
      flatten(item) if item.class == Array
      final << item
    end
    final.compact
  end
end
