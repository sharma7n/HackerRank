# Enter your code here. 
hackerrank[543121] = 100
hackerrank.keep_if {|key, _| key.is_a? Integer}
hackerrank.delete_if {|key, _| key % 2 == 0}