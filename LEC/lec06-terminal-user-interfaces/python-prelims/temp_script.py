from temp_utils import *
celsius_values = range(0,55,5)

print("Celsius\tFahrenheit")
for celsius in celsius_values:
    print(f"{celsius}\t{c_to_f(celsius)}")  
    