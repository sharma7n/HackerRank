# Enter your code here
def strike(word)
    "<strike>#{word}</strike>"
end

def mask_article(article, to_strike)
    to_strike.each do |word|
        article = article.gsub(word, strike(word))
    end
    article
end