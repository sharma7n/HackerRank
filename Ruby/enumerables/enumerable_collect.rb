$alphabet = ('a'..'z').to_a

def rot13_char(char)
    if $alphabet.include? char
        index = $alphabet.index(char)
        new_index = (index + 13) % $alphabet.length
        new_char = $alphabet[new_index]
        new_char
    else
        return char
    end
end

def rot13_word(word)
    word.map{|char| rot13_char(char)}.join('')
end

def rot13(secret_messages)
  # your code here
    secret_messages.map {|word| rot13_word(word.chars)}
end