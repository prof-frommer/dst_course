def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    temp = float(input("Enter temperature in Celsius: "))
    print(f"In Fahrenheit: {c_to_f(temp)}")
    
