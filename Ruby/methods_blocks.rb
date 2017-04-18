def factorial
    yield
end

def _factorial(k)
    if k <= 1
        1
    else
        k * _factorial(k - 1)
    end
end

n = gets.to_i
factorial do 
    puts _factorial n
end