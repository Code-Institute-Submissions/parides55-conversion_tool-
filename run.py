import requests
import json
import sys
import sympy.physics.units as u
import mpmath
sys.modules['sympy.mpmath'] = mpmath

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


def validate_selection(sel):
    """
    Validates the user's input.
    """
    try:
        if sel != '1' and sel != '2' or isinstance(sel, str) is False:
            raise ValueError(
                f'Select 1 for Curency or 2 for Unit Conversion.'
                f'You have selected "{sel}"'
                )
    except ValueError as e:
        print(f'Invalid Selection! {e}')
        return False

    return True


def check_currency_codes(value1, value2):
    try:
        if value1 not in dict_currency:
            raise ValueError(f'Please type a code from the list above.'
                             f'For example, for euros type EUR.'
                             f'You have typed "{value1}"')
        if value2 not in dict_currency:
            raise ValueError(f'Please type a code from the list above.'
                             f'For example, for euros type EUR.'
                             f'You have typed "{value2}"')
        if value1 == value2:
            raise ValueError(f'Please select different values.'
                             f' You have selected the same values')
    except ValueError as e:
        print(f"Wrong Input!{e}")
        return False

    return True


def check_amount(currency):
    try:
        if [float(currency)] == str:
            raise ValueError(
                f'Please enter a number. You have entered "{currency}"'
                )
    except ValueError as e:
        print(f'Enter a number. {e}')
        return False

    return True


def check_category(num):
    try:
        if num != '1' and num != '2' or isinstance(num, str) is False:
            raise ValueError(
                f'Select 1 for Length Conversion or 2 for Mass Conversion.'
                f'You have selected "{num}"'
                )
    except ValueError as e:
        print(f'Invalid Selection! {e}')
        return False

    return True


def check_unit(num1, num2):
    AVAIL_CONVER = AVAILABLE_CONVERSIONS_LENGTH + AVAILABLE_CONVERSIONS_MASS
    try:
        if num1 not in AVAIL_CONVER:
            raise ValueError(f'Please select a unit from the above list.'
                             f' You have input {num1}')
        if num2 not in AVAIL_CONVER:
            raise ValueError(f'Please select a unit from the above list.'
                             f' You have input {num2}')
        if num1 == num2:
            raise ValueError(f'Please select different values.'
                             f' You have selected the same values')
    except ValueError as e:
        print(f'Wrong Input!{e}')
        return False
    return True


def check_value(val):
    try:
        if [float(val)] == str:
            raise ValueError(
                f'Please enter a number. You have entered "{val}"'
                )
    except ValueError as e:
        print(f'Invalid input. {e}')
        return False
    return True


def check_run_again_input(x):
    try:
        if x != 'yes' and x != 'no':
            raise ValueError(f'Please selecte "yes" or "no"'
                             f' You have typed "{x}"')
    except ValueError as e:
        print(f'Invalid input! {e}')
        return False
    return True


def run_again():
    """
    A function which is called after every conversion is made
    and gives the option to the user to choose to continue
    making another conversion or exit the program.
    """
    print()
    while True:
        answer = input(
            "Would you like to make another conversion? (yes/no)\n").lower()
        if (check_run_again_input(answer)):
            if answer == 'yes':
                start_up()
                break
            else:
                print()
                print("Thank you for using the CONVERSION TOOL\n")
                break
    return None


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
            select_category()
            break

    return None


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
            while True:
                str_amount = input(
                 f'Enter an amount of {from_rate} to convert to {to_rate} :'
                )
                if (check_amount(str_amount)):
                    amount = float(str_amount)
                    amount_converted = requests.get(
                        f'https://api.frankfurter.app/latest?amount={amount}'
                        f'&from={from_rate}&to={to_rate}'
                        )
                    print(
                        f"{amount} {from_rate} is"
                        f"{amount_converted.json()['rates'][to_rate]}"
                        f"{to_rate}"
                        )
                    run_again()
                    break
            return None


def select_category():
    """
    When it's called shows the availabel unit conversions and
    asks the user to make inputs. These inputs then are passed to the
    Calculator class.
    """
    print()
    print('UNIT CONVERSION\n')
    print('CATEGORIES')
    print()
    for x, y in CATEGORIES:
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


def mass_selection():
    print()
    print('Available Conversion')
    print(AVAILABLE_CONVERSIONS_MASS)
    print()
    while True:
        unit_from = input("Enter a unit you would like to convert from :")
        unit_to = input("Enter a unit you would like to convert to :")

        if check_unit(unit_from, unit_to):
            while True:
                str_value = input(
                    f"Enter an amount of {unit_from} to convert to {unit_to}:")
                if (check_value(str_value)):
                    value = float(str_value)
                    to_calculate = Calculator(unit_from, unit_to, value)
                    to_calculate.mass_calculation()
                    break
            return None


def lengtn_selection():
    print()
    print('Available Conversion')
    print(AVAILABLE_CONVERSIONS_LENGTH)
    print()
    while True:
        unit_from = input("Enter a unit you would like to convert from :")
        unit_to = input("Enter a unit you would like to convert to :")

        if check_unit(unit_from, unit_to):
            while True:
                str_value = input(
                    f"Enter an amount of {unit_from} to convert to {unit_to}:")
                if (check_value(str_value)):
                    value = float(str_value)
                    to_calculate = Calculator(unit_from, unit_to, value)
                    to_calculate.length_calculation()
                    break
            return None


class Calculator:

    def __init__(self, unit_from, unit_to, value):
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.value = value

    def length_calculation(self):
        if self.unit_from == 'km' and self.unit_to == 'meters':
            answer = u.convert_to(self.value * u.km, u.meters).n()
            print(f'{self.value} {self.unit_from} is {answer}')
        elif self.unit_from == 'meters' and self.unit_to == 'km':
            answer = u.convert_to(self.value * u.meters, u.km).n()
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
