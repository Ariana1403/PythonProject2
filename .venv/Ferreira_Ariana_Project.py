#Ariana Ferreira
#Project :  Lego Inventory System
#Description : This program manages LEGO sets in a inventory System

#Import the validation functions
from validation import read_lego_code, read_valid_lego_name,read_integer, read_float, read_valid_option

# Function to Load LEGO data from a file

def load_lego_data(file_name):
    lego_data = []

    try:
        with open(file_name, 'r', encoding= 'utf-8') as file:
            for line in file:
                data = line.strip().split(',')

                #Create a dictionary for each Lego Set
                lego_set = {
                    'set_number' : data[0],
                    'title' : data[1],
                    'pieces' : int(data[2]),
                    'price' : float(data[3]),
                    'stock_status' : int(data[4]),
                }

                lego_data.append(lego_set)

        return lego_data

    except FileNotFoundError:
        print(f"Errot: The file{file_name} was not found")
        return[]

    except Exception as e:
        print(f"An unnexpectated error occured {e}")

# Function to save LEGO data to a file

def save_lego_data(file_name, lego_data):
    try:
        with open(file_name, 'w', enconding='utf-8') as file:
            for lego_set in lego_data:
                file.write(f"{lego_set['set_number']},{lego_set['title']},{lego_set['piecces']}, {lego_set['price']}, {lego_set['stock_status']}\n")
                print("Data saved sucessfully.")
    except Exception as e:
        print(f"Error saving data: {e}")


#Function to display inventory

def display_inventory(lego_data):
    print("\nLego Sets")
    print("-" * 80)

    for lego_set in lego_data:
        set_number = lego_set['set_number']
        title = lego_set['title']
        pieces = f"{lego_set['pieces']:,}"
        price = lego_set['price']

        if lego_set['stock_status'] == 1:
            stock_icon = '✅'
        else:
            stock_icon ='❌'

        retired_market = ""

        if lego_set['price'] == 0.00:
            retired_market = '#'

        print(f"{set_number:<7} {title:<40}  {pieces:<8} {stock_icon:^5} {price:>8.2f} {retired_market}")

#Function do add a new LEGO  set:

def add_new_lego_set(lego_data, file_name):
    print("\nAdd New LEGO Set")

    new_set_number = read_lego_code("Enter the LEGO set number (5-7 digits): ")

    for lego_set in lego_data:
        if lego_set['set_number']  == new_set_number:
            print(f"Error: LEGO set number {new_set_number} already exist.")
            return

# Get additional details with validation

    title = read_valid_lego_name("Enter the Lego set title: ")
    pieces = read_integer("Enter the number of pieces: ", 1, 5000)
    price = read_float("Enter the price (0.00 for retired sets): ",0.0, 500.0)
    stock_status = read_valid_option("Enter stock status (1 for in stock, o for out of stock): ", ['0', '1'])

 # Add the new Lego Set to the lego_data list
    new_lego_set = {
        'set_number' : new_set_number,
        'title' : title,
        'pieces' : pieces,
        'price': price,
        'stock_status': int(stock_status),
    }
    lego_data.append(new_lego_set)

    print(f"Sucessfull added new LEGO set: {new_set_number} - {title}")








lego_data= load_lego_data('lego_data.txt')
file_name = 'lego_data.txt'
display_inventory(lego_data)
add_new_lego_set(lego_data, file_name)