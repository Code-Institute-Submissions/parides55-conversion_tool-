import requests
import json

def make_selection():
    """
    This function takes user's selections, 
    validates the selection made from the user by calling the validate_conversion_selection function 
    and calls the approprite conversion function.
    """
    
    while True:        
        print()
        conversion_selection = input('Select a number:\n')
        if validate_conversion_selection(conversion_selection):
            print("Valid selection")

        if conversion_selection == '1':
            calculate_currency()
            break
        elif conversion_selection == '2':
            print()
            print('UNIT CONVERSION\n')
            unit_from = input("Enter a unit you would like to convert from :")
            unit_to = input("Enter a unit you would like to convert to :")
            value = int(input(f"Enter the amount of {unit_from} to convert to {unit_to} :"))
            to_calculate = Calculator(unit_from, unit_to, value)
            to_calculate.make_conversion()
            break
        
    return conversion_selection
    
def validate_conversion_selection(selection):
    """
    Validates the user's input.
    """
    try:
        if selection != '1' and selection != '2' or isinstance(selection, str) == False:
            raise ValueError(
                f'Please select 1 for Curency Conversion or 2 for Unit Conversion. You have selected "{selection}"'
                )
    except ValueError as e:
        print(f'Invalid Selection! {e}')
        return False
    
    return True

def repeat():
    """
    A function which is called after every conversion is made and gives the option to
    the user to choose to continue making another conversion or exit the program. 
    """
    print()
    answer = input("Would you like to make another conversion? (yes/no)\n").lower()
    
    if answer == 'yes':
        start_up()
    else:
        print()
        print("Thank you for using the CONVERSION TOOL\n")

def calculate_currency():
    """
    Takes the currency codes and the value that the user wants to convert
    and makes the conversion using the frankfurter API.
    """
    print()
    print('CURRENCY CONVERSION\n')
    
    url = "https://api.frankfurter.app/currencies"
    response_currencies = requests.request("GET", url)
    dict_currency = json.loads(response_currencies.text)
    list_currency = list(dict_currency.keys())
    print('Available Currency Codes to use\n')
    print(list_currency)
    print()
     
    from_rate = str(input("Enter the currency code you would like to convert from (eg.EUR) :").upper())
    to_rate = str(input("Enter the currency code you would like to convert to (eg.USD) :").upper())
    # validate_currency_inputs()
    amount = float(input(f'Enter the amount of {from_rate} you would like to convert to {to_rate} :'))
    amount_converted = requests.get(f'https://api.frankfurter.app/latest?amount={amount}&from={from_rate}&to={to_rate}')
    
    print(f"{amount} {from_rate} is {amount_converted.json()['rates'][to_rate]} {to_rate}")
    
    repeat()
 
class Calculator:
    """
    Takes the values and units and makes the conversion.
    """
    
    def __init__(self, unit_from, unit_to, value):
        # properties
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.value = value
        # validate_conversion_inputs()
    
    def make_conversion(self):
        """
        Takes the units and the value entered from the user to make the conversion.
        """    
        if self.unit_from == 'kilometres' and self.unit_to == 'metres':
            converted_value = self.value * 1000
        elif self.unit_from == 'kilometres' and self.unit_to == 'miles':
            converted_value = self.value * 1.60934
        elif self.unit_from == 'metres' and self.unit_to == 'kilometres':
            converted_value = self.value / 1000
        elif self.unit_from == 'metres' and self.unit_to == 'miles':
            converted_value = self.value * 0.000621371
        elif self.unit_from == 'miles' and self.unit_to == 'kilometres':
            converted_value = self.value * 1.60934
        elif self.unit_from == 'miles' and self.unit_to == 'metres':
            converted_value = self.value * 1609.34
            
        print(f'{self.value} {self.unit_from}  =  {converted_value:.2f} {self.unit_to}')
        
        repeat()
    
        
def start_up():
    """
    Run all programms
    """
    CONVERSINOS = [
        ('(1)', 'Currency Conversion'),
        ('(2)', 'Unit Conversion'),
    ]
    
    print("What would you like to convert?")
    print()

    for num, conversion in CONVERSINOS:
        print(f'{num} -- {conversion}')
    make_selection()        
    
print("CONVERSION TOOL")
print()
start_up()    