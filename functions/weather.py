# x = Expected output = Temperature in celcius
# y = The given Value = Temperature in Fahrenheit
# function(y) = formula I need to calculate x = ??? = (temperature_f - 32) * (5/9)

def convert_temp_in_f_to_c(temperature_f):
    temperature_in_celcius = (temperature_f - 32) * (5/9)
    return temperature_in_celcius

def function(y):
    x = (y - 32) * (5/9)
    return x

print(convert_temp_in_f_to_c(0))    