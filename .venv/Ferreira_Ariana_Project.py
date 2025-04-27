#Ariana Ferreira
#Project :  Lego Inventory System
#Description : This program manages LEGO sets in a inventory System

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

    except FileNotFoundError:
        print(f"Errot: The file{lego_data} was not found")
        return[]

    except Exception as e:
        print(f"An unnexpectated error occured {e}")

    return lego_data

lego_inventory = load_lego_data('lego_data.txt')

for lego_set in lego_inventory:
    print(lego_set)