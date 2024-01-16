import requests

def make_selection():
    CONVERSINOS = [
        ('(1)', 'Currency Conversion'),
        ('(2)', 'Unit Conversion'),
    ]
    
    print("What would you like to convert?")
    print()

    for num, conversion in CONVERSINOS:
        print(f'{num} -- {conversion}')
        
    print()
    conversion_selection = int(input('Select a number:\n'))

    if conversion_selection == 1:
        calculate_currency()
    elif conversion_selection == 2:
        print()
        print('UNIT CONVERSION\n')
        unit_from = input("Enter a unit you would like to convert from :")
        unit_to = input("Enter a unit you would like to convert to :")
        value = int(input(f"Enter the amount of {unit_from} to convert to {unit_to} :"))
        unit_conversion = Calculator(unit_from, unit_to, value)
        return unit_conversion.test()
    else:
        print("Wrong input!")

def repeat():
    answer = input("Would you like to make another conversion?\n").lower()
    
    if answer == 'yes':
        start_up()
    else:
        print("Thank you for using the CONVERSION TOOL")

def calculate_currency():
    print()
    print('CURRENCY CONVERSION\n')
     
    from_rate = str(
         input("Enter the currency code you would like to convert from (eg.EUR) :").upper()
     )
     
    to_rate = str(
        input("Enter the currency code you would like to convert to (eg.USD) :").upper()
    )
    
    amount = float(
        input(f'Enter the amount of {from_rate} you would like to convert to {to_rate} :')
    )
    
    amount_converted = requests.get(
        f'https://api.frankfurter.app/latest?amount={amount}&from={from_rate}&to={to_rate}'
    )
    
    print(
        f"{amount} {from_rate} is {amount_converted.json()['rates'][to_rate]} {to_rate}"
    )
    
    repeat()
 
class Calculator:
    """
    Takes the values and makes the conversions
    """
    
    def __init__(self, unit_from, unit_to, value):
        # properties
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.value = value
    
    def test(self):
        print(f'{self.value}{self.unit_from} is {self.unit_to}')    
        repeat()
    

        
def start_up():
    """
    Run all programms
    """
    make_selection()        
    
print("CONVERSION TOOL")
print()
start_up()    