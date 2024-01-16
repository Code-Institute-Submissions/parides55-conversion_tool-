def make_selection():
    CONVERSINOS = [
        ('(1)', 'Currency'),
        ('(2)', 'Distance'),
        ('(3)', 'Weight'),
        ('(4)', 'Speed'),
        ('(5)', 'Volume'),
        ('(6)', 'Area'),
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
        calculate_distance()
    elif conversion_selection == 3:
        calculate_weight()
    elif conversion_selection == 4:
        calculate_speed()
    elif conversion_selection == 5:
        calculate_volume()
    elif conversion_selection == 6:
        calculate_area()
    else:
        print("Wrong input!")

def calculate_currency():
     print()
     print('Currency')

def calculate_distance():
     print()
     print('Distance')
     
def calculate_weight():
     print()
     print('Weight')
     
def calculate_speed():
     print()
     print('Speed')
     
def calculate_volume():
     print()
     print('Volume')
     
def calculate_area():
    print()
    print('Area')
 
 
     
def start_up():
    make_selection()
    
print("CONVERSION TOOL")
print()
start_up()