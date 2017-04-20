def sum_terms(n)
  # your code here
    (1..n).reduce(0) { |sum, i| sum + (i*i + 1) } 
end
