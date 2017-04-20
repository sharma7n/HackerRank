def count_multi_byte(s)
    s.each_char.select { |char| char.bytesize > 1 }.count
end