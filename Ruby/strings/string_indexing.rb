# Your code here
def serial_average(s)
    serial = s[0, 3]
    x = s[4, 5]
    y = s[10, 5]
    average = (x.to_f + y.to_f) / 2.0
    "#{serial}-#{format('%.2f', average.round(2))}"
end