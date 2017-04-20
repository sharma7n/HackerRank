def to_celsius(temperature, input_scale: 'celsius')
    if input_scale == 'celsius'
        temperature
    elsif input_scale == 'fahrenheit'
        (temperature - 32) / 1.8
    elsif input_scale == 'kelvin'
        temperature - 273.15
    else
        raise "Unknown Temperature Input Scale"
    end
end

def from_celsius(temperature, output_scale: 'celsius')
    if output_scale == 'celsius'
        temperature
    elsif output_scale == 'fahrenheit'
        (temperature * 1.8) + 32
    elsif output_scale == 'kelvin'
        temperature + 273.15
    else
        raise "Unknown Temperature Output Scale"
    end
end

def convert_temp(temperature, **scales)
    from_celsius(to_celsius(temperature, input_scale: scales[:input_scale]), output_scale: scales[:output_scale]) 
end