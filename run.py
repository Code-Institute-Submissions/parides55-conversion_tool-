import requests
import json
import sys
import mpmath
sys.modules['sympy.mpmath'] = mpmath
import sympy.physics.units as u

CONVERSINOS = [
        ('(1)', 'Currency Conversion'),
        ('(2)', 'Unit Conversion'),
    ]
AVAILABLE_CONVERSIONS_LENGTH = ['feet', 'miles', 'inches', 'meters', 'km'] 
AVAILABLE_CONVERSIONS_MASS = ['grams', 'tonne', 'pounds', 'kg'] 
CATEGORIES = [
    ('(1)', 'Length'),
    ('(2)', 'Mass')
]

# fetches a dictionary of all currencies used in the frankfurter api
# and returns a list
url = "https://api.frankfurter.app/currencies"
response_currencies = requests.request("GET", url)
dict_currency = json.loads(response_currencies.text)
list_currency = list(dict_currency.items())
def run_again():
    """
    A function which is called after every conversion is made
    and gives the option to the user to choose to continue
    making another conversion or exit the program.
    """
    print()
    answer = input(
        "Would you like to make another conversion? (yes/no)\n").lower()

    if answer == 'yes':
        start_up()
    else:
        print()
        print("Thank you for using the CONVERSION TOOL\n")


def make_selection():
    """
    This function takes user's selections,
    validates the selection made from the user by calling the
    validate_conversion_selection function
    and calls the approprite conversion function.
    """

    while True:
        print()
        conversion_selection = input('Select a number:\n')
        if validate_selection(conversion_selection):
            print("Valid selection")

        if conversion_selection == '1':
            calculate_currency()
            break
        elif conversion_selection == '2':
            start_unit_conversions()
            break

    return None


def validate_selection(selection):
    """
    Validates the user's input.
    """
    try:
        if selection != '1' and selection != '2' or isinstance(selection, str) is False:
            raise ValueError(
                f'Select 1 for Curency or 2 for Unit Conversion.'
                f'You have selected "{selection}"'
                )
    except ValueError as e:
        print(f'Invalid Selection! {e}')
        return False

    return True


def check_currency_codes(value1, value2):
    try:
        if not value1 in dict_currency:
            raise ValueError(f'Please type a code from the list above.'
                f'For example, for euros type EUR.'
                f'You have typed "{value1}"')
        if not value2 in dict_currency:
            raise ValueError(f'Please type a code from the list above.'
                f'For example, for euros type EUR.'
                f'You have typed "{value2}"')
    except ValueError as e:
        print(f"Wrong Input!{e}")
        return False

    return True


def calculate_currency():
    """
    Takes the currency codes and the value that the user wants to convert
    and makes the conversion using the frankfurter API.
    """
    print()
    print('CURRENCY CONVERSION\n')
    print('Available Currency Codes to use\n')
    print(list_currency)
    print()

    while True:
        
        from_rate = str(input(
            "Enter a currency code to convert from (eg.EUR) :").upper())
        to_rate = str(input(
            "Enter a currency code to convert to (eg.USD) :").upper())
        
        if (check_currency_codes(from_rate, to_rate)):
            amount = float(input(
                f'Enter an amount of {from_rate} to convert to {to_rate} :'
                ))
            amount_converted = requests.get(
                f'https://api.frankfurter.app/latest?amount={amount}&from={from_rate}&to={to_rate}'
                )
            print(
                f"{amount} {from_rate} is {amount_converted.json()['rates'][to_rate]} {to_rate}"
                )
            run_again()
            break

    return None   


def start_unit_conversions():
    """
    When it's called shows the availabel unit conversions and
    asks the user to make inputs. These inputs then are passed to the
    Calculator class.
    """
    print()
    print('UNIT CONVERSION\n')
    print('CATEGORIES')
    print()
    for x,y in CATEGORIES:
        print(f'{x} - {y}')

    while True:

        category_input = input("Choose a category to satrt :")

        if check_category(category_input):
            if category_input == '1':
                lengtn_selection()
                break
            if category_input == '2':
                mass_selection()
                break
                
    return None


def check_category(num):
    try:
        if num != '1' and num != '2' or isinstance(num, str) is False:
            raise ValueError(
                f'Select 1 for Length Conversio or 2 for Mass Conversio.'
                f'You have selected "{num}"'
                )
    except ValueError as e:
        print(f'Invalid Selection! {e}')
        return False

    return True


def check_value(num1, num2):
    AVAILABLE_CONVERSIONS = AVAILABLE_CONVERSIONS_LENGTH + AVAILABLE_CONVERSIONS_MASS
    try:
        if not num1 in AVAILABLE_CONVERSIONS:
            raise ValueError(f'Please select a unit from the above list. You have input {num1}')
        if not num2 in AVAILABLE_CONVERSIONS:
            raise ValueError(f'Please select a unit from the above list. You have input {num2}')
        if num1 == num2:
            raise ValueError('Please select different values. You have selected the same values')
    except ValueError as e:
        print(f'Wrong Input!{e}')
        return False
    return True


def mass_selection():
    print()
    print('Available Conversion')
    print(AVAILABLE_CONVERSIONS_MASS)
    print()
    while True:
        unit_from = input("Enter a unit you would like to convert from :")
        unit_to = input("Enter a unit you would like to convert to :")
        
        if check_value(unit_from, unit_to):
            value = int(input(
                f"Enter the amount of {unit_from} to convert to {unit_to} :"))
            to_calculate = Calculator(unit_from, unit_to, value)
            to_calculate.mass_calculation()
            break


def lengtn_selection():
    print()
    print('Available Conversion')
    print(AVAILABLE_CONVERSIONS_LENGTH)
    print()
    while True:
        unit_from = input("Enter a unit you would like to convert from :")
        unit_to = input("Enter a unit you would like to convert to :")
        
        if check_value(unit_from, unit_to):
            value = int(input(
                f"Enter the amount of {unit_from} to convert to {unit_to} :"))
            to_calculate = Calculator(unit_from, unit_to, value)
            to_calculate.dist_calculation()
            break


class Calculator:
    
    def __init__(self, unit_from, unit_to, value):
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.value = value
        
    def dist_calculation(self):
        if self.unit_from == 'km' and self.unit_to == 'metres':
            answer = u.convert_to(self.value * u.km, u.m).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'metres' and self.unit_to == 'km':
            answer = u.convert_to(self.value * u.m, u.km).n()
            print(f'{self.value} {self.unit_from} is {answer}') 
        elif self.unit_from == 'km' and self.unit_to == 'miles':
            answer = u.convert_to(self.value * u.km, u.miles).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'miles' and self.unit_to == 'km':
            answer = u.convert_to(self.value * u.miles, u.km).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'km' and self.unit_to == 'feet':
            answer = u.convert_to(self.value * u.km, u.feet).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'feet' and self.unit_to == 'km':
            answer = u.convert_to(self.value * u.feet, u.km).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'km' and self.unit_to == 'inches':
            answer = u.convert_to(self.value * u.km, u.inches).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'inches' and self.unit_to == 'km':
            answer = u.convert_to(self.value * u.inches, u.km).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'miles' and self.unit_to == 'feet':
            answer = u.convert_to(self.value * u.miles, u.feet).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'feet' and self.unit_to == 'miles':
            answer = u.convert_to(self.value * u.feet, u.miles).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'miles' and self.unit_to == 'meters':
            answer = u.convert_to(self.value * u.miles, u.meters).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'meters' and self.unit_to == 'miles':
            answer = u.convert_to(self.value * u.meters, u.miles).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'miles' and self.unit_to == 'inches':
            answer = u.convert_to(self.value * u.miles, u.inches).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'inches' and self.unit_to == 'miles':
            answer = u.convert_to(self.value * u.inches, u.miles).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'meters' and self.unit_to == 'inches':
            answer = u.convert_to(self.value * u.meters, u.inches).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'inches' and self.unit_to == 'meters':
            answer = u.convert_to(self.value * u.inches, u.meters).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'meters' and self.unit_to == 'feet':
            answer = u.convert_to(self.value * u.meters, u.feet).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'feet' and self.unit_to == 'meters':
            answer = u.convert_to(self.value * u.feet, u.meters).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'inches' and self.unit_to == 'feet':
            answer = u.convert_to(self.value * u.inches, u.feet).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'feet' and self.unit_to == 'inches':
            answer = u.convert_to(self.value * u.feet, u.inches).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        run_again()
            
    def mass_calculation(self):
        if self.unit_from == 'kg' and self.unit_to == 'grams':
            answer = u.convert_to(self.value * u.kg, u.grams).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'grams' and self.unit_to == 'kg':
            answer = u.convert_to(self.value * u.grams, u.kg).n()
            print(f'{self.value} {self.unit_from} is {answer}') 
        elif self.unit_from == 'kg' and self.unit_to == 'tonne':
            answer = u.convert_to(self.value * u.kg, u.tonne).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'tonne' and self.unit_to == 'kg':
            answer = u.convert_to(self.value * u.tonne, u.kg).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'kg' and self.unit_to == 'pounds':
            answer = u.convert_to(self.value * u.kg, u.pound).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'pounds' and self.unit_to == 'kg':
            answer = u.convert_to(self.value * u.pound, u.kg).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'pounds' and self.unit_to == 'grams':
            answer = u.convert_to(self.value * u.pound, u.grams).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'grams' and self.unit_to == 'pounds':
            answer = u.convert_to(self.value * u.grams, u.pound).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'pounds' and self.unit_to == 'tonne':
            answer = u.convert_to(self.value * u.pound, u.tonne).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'tonne' and self.unit_to == 'pound':
            answer = u.convert_to(self.value * u.tonne, u.pound).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'grams' and self.unit_to == 'tonne':
            answer = u.convert_to(self.value * u.grams, u.tonne).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'tonne' and self.unit_to == 'grams':
            answer = u.convert_to(self.value * u.tonne, u.grams).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        run_again()


def start_up():
    """
    Run all programms
    """
    print("What would you like to convert?")
    print()

    for num, conversion in CONVERSINOS:
        print(f'{num} -- {conversion}')
    make_selection()


print("CONVERSION TOOL")
print()
start_up()
