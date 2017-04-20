def factorial(m)
    (1..m).reduce(1, :*)
end

combination = -> (_n) do
    -> (_k) do
        factorial(_n) / (factorial(_k) * factorial(_n - _k))
    end
end
        

n = gets.to_i
r = gets.to_i
nCr = combination.(n)
puts nCr.(r)
