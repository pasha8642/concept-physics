class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def get_numerator(self, denominator):
        self.denominator = denominator

    def access_numerator(self):
        return self.numerator

    def access_denominator(self):
        return self.denominator

    def add(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def subtraction(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator - other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def multiplication(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return  Fraction(new_numerator, new_denominator)



    def division(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return Fraction(new_numerator, new_denominator)

    def conclusion(self):
        return f'{self.numerator} / {self.denominator}'

class Conversion:
    @staticmethod
    def fahrenheit_to_Celsius(temp):
        fahrenheit = temp * 1.8 + 32
        return fahrenheit

    @staticmethod
    def Celsius_to_fahrenheit(temp):
        celsius = (temp - 32) / 1.8
        return celsius

class MetricSystem:
    @staticmethod
    def liters_to_us_gallons(liters):
        conversion_factor = 3.78541
        gallons = liters * conversion_factor
        return gallons

    @staticmethod
    def miles_to_km(miles):
        conversion_rate = 1.609344
        kilometers = miles * conversion_rate
        return kilometers

    @staticmethod
    def km_to_miles(km):
        conversion_rate = 0.62137119
        miles = km * conversion_rate
        return miles

    @staticmethod
    def gallon_to_liters(gallon):
        conversion_rate = 0.264172
        liters = gallon * conversion_rate
        return liters



drob = Fraction(10, 10)
drob1 = Fraction(9, 10)
result = drob.division(drob1)
print(result.conclusion())










        








