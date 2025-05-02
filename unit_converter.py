# python-projects
def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("Sample Conversions:")
print("5 KM = ", km_to_miles(5), "Miles")
print("3 Miles = ", miles_to_km(3), "KM")
print("100°C = ", celsius_to_fahrenheit(100), "°F")
print("212°F = ", fahrenheit_to_celsius(212), "°C")
