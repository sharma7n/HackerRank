# Enter your code here. Read input from STDIN. Print output to STDOUT
def process_text(text)
    text.map { |word| word.strip.chomp }.join(" ")
end