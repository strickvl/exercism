class FlattenArray
  def self.flatten(arr)
    arr.flatten.reject {|val| val == nil}
  end
end
