import requests

def make_selection():
    """
    This function gives selections to the user to choose what conversion to use.
    """
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
        unit_from = input("Enter a unit you would like to convert from :").lower()
        unit_to = input("Enter a unit you would like to convert to :").lower()
        value = int(input(f"Enter the amount of {unit_from} to convert to {unit_to} :"))
        unit_conversion = Calculator(unit_from, unit_to, value)
        return unit_conversion.make_conversion()
    else:
        print("Wrong input!")

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
    Takes the values and units and makes the conversion.
    """
    
    def __init__(self, unit_from, unit_to, value):
        # properties
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.value = value
    
    def make_conversion(self):
        """
        Takes the units and the value entered from the user to make the conversion.
        """    
        if self.unit_from == 'kilometres' and self.unit_to == 'metre':
            converted_value = self.value * 1000
        elif self.unit_from == 'kilometres' and self.unit_to == 'miles':
            converted_value = self.value * 0.6214
        
        print(f'{self.value} {self.unit_from}  =  {converted_value:.2f} {self.unit_to}')
        
        repeat()
    

        
def start_up():
    """
    Run all programms
    """
    make_selection()        
    
print("CONVERSION TOOL")
print()
start_up()    