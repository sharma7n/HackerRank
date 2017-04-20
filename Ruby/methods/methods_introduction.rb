# Your code here
def prime?(number)
    if number < 2
        return false
    end
    
    (2..number - 1).each do |k|
        if number % k == 0
            return false
        end
    end
    
    true
end