# Enter your code here. Read input from STDIN. Print output to STDOUT
# FAILS test cases 1, 2, and 3 (only passes 0)

n = $stdin.read.to_i

def is_palindrome(num)
    repr = num.to_s
    if repr == repr.reverse!
        return true
    else
        return false
    end
end

def is_prime(num)
    prime = true
    2.upto(num - 1).lazy.each do |k|
        if num % k == 0
            prime = false
            break
        end
    end
    return prime
end

palindromic_primes = -> (num) do
    2.upto(Float::INFINITY).lazy.select {|i| is_prime(i) and is_palindrome(i) } .first(num)
end

print palindromic_primes.(n)