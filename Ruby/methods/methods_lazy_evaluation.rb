# Enter your code here. Read input from STDIN. Print output to STDOUT
require 'set'

n = gets.to_i

$primes = Set.new
def is_prime?(k)
    if k <= 1
        false
    elsif $primes.include? k
        true
    else
        (2..Math.sqrt(k))
            .lazy
            .each do |i|
            if k % i == 0
                return false
            end
        end
        $primes.add(k)
        true
    end
end

def is_palindrome?(k)
    k.to_s == k.to_s.reverse
end


print 1
    .upto(Float::INFINITY)
    .lazy
    .select { |a| is_palindrome? a }
    .select { |b| is_prime? b }
    .first(n)