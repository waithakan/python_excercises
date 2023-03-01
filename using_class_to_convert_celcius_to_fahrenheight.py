# create a class called temperature and make two methods:
# i) convertFahrenheit - it will take celcius and print it into fahrenheit
# ii) convertcelcius - it will take fahrenheit and convert it to celcius

#program to convert farenheit to celcius and celcius to farenheit
celcius = float(input("Enter temperature in celcius: "))
farenheit = float(input("Enter temperature in farenheit: "))
class Temperature: 
    def __init__(self,celcius, farenheit):
        self.celcius = celcius
        self.farenheit = farenheit

    def convertFarenheit (self):
        return ((self.celcius * 9/5)+32)
    def convertCelcius (self):
        return ((self.farenheit - 32 ) * (5/9))
    
T = Temperature(celcius, farenheit)
print("Conversion from ceclius to farenheit is = " ,T.convertFarenheit())
print("Conversion from cfarenheit to celcius is = " ,T.convertCelcius())
