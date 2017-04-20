def skip_animals(animals, skip)
  # Your code here
    filtered = []
    animals.each_with_index do |animal, index|
        if index >= skip
            filtered.push("#{index}:#{animal}")
        end
    end
    filtered
end
