''' this is project_2 that contains basic back-end for furniture-marketplace '''
import json
filename = "furnitures.json"
def load_listings():
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
def save_listings(furnitures):
    with open(filename, "w") as file:
        json.dump(furnitures,file, indent=4)

def add_listings(furnitures):
    
    while True:
        name = input("Enter furniture name: ").strip()
        if name and all(char.isalpha() or char.isspace() for char in name):
            break   
        else:
            print("only letters and spaces allowed")
            
    while True:   
        seller_name = input("Enter seller name: ").strip()
        if seller_name and all(char.isalpha() or char.isspace() for char in  seller_name):
            break
        else:
            print("only letter and space allowed")
            
    while True:
        city = input("Enter you city: ").strip()
        if city and all(char.isalpha() or char.isspace() for char in  city):
            break
        else:
            print("only letter and space allowed")
            
    while True:
        try:
            price = float(input("enter price: "))
            break
        except ValueError:
            print("plase enter only numbers !")  

    item = {
        "name": name,
        "seller_name": seller_name,
        "city": city,
        "price": price
    }  

    furnitures.append(item)
    save_listings(furnitures)

def view_listings(furnitures):
    for item in furnitures:
      print(f" name: {item['name']} | seller name: {item['seller_name']} | city: {item['city']} | price:  {item['price']:,} uzs")


def search_listings(furnitures):
    while True:
        keyword = input("Enter furniture name to search: ").strip().lower()
        if keyword and all(char.isalpha() or char.isspace() for char in keyword):
            break
        print("only leters are allowed !")
        keyword = input("Enter furniture name to search: ").strip().lower()

    results = [item for item in furnitures if keyword in item["name"].lower()]
    if results:
        for item in results:
            print(f" name: {item['name']} | seller name: {item['seller_name']} | city: {item['city']} | price:  {item['price']:,} uzs")
    else:
            print("furniture is not found")


def main():
    furnitures = load_listings()
    print("welcome to our program !")
    print("-- add furnitures --")
    print("-- view all available items --")
    print("-- search for items --")
    print("-- exit --")
    while True:
        

        choice = input("enter 1-4: ")

        if choice == "1":
            add_listings(furnitures)
        
        elif choice == "2":
            view_listings(furnitures)

        elif choice == "3":
            search_listings(furnitures)

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("invalid input please only enter 1-4 !")
        
        
            
main()