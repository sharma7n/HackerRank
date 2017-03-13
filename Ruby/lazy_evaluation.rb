# Enter your code here. Read input from STDIN. Print output to STDOUT
# FAILS test cases 1, 2, and 3 (only passes 0)

# n = $stdin.read.to_i

def is_palindrome(num)
    reversed = num.to_s.reverse!.to_i
    return num == reversed
end

def is_prime(num)
    prime = true
    2.upto((num + 1) / 2).lazy.each do |k|
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

start = Time.now
print palindromic_primes.(80)
elapsed = Time.now - start
puts elapsed