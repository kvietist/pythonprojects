''' this project 1 that makes books lists '''
import json
filename = "books.json"

def load_books():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(filename, "w") as file:
        json.dump(books,file, indent=4)

def add_book(books):
    print("\nadd_book")
    
    name = input("enter book name: ").strip()
    while True:
        if name and all(char.isalpha() or char.isspace() for char in name):
           break
        print("only letters and space is allowed !")
        name = input("enter book name: ").strip()
    
    author = input("enter book author: ").strip()
    while True:
        if author and all(char.isalpha() or char.isspace() for char in author):
           break
        print("only letters and space is allowed !")
        author = input("enter book author: ").strip()
    while True:
        try:
         price = float(input("Enter book price (uzs): "))
         break
        except ValueError:
          print("plase enter only numbers")

    item = {
        "name": name,
        "author": author,
        "price": price
    }
    books.append(item)
    save_books(books)
    print(f"{name} added successfully !")
def search_book(books):
    print("\nsearch_book")
    while True:
        keyword = input("Enter book name to search: ").strip().lower()
        if keyword and all(char.isalpha() or char.isspace() for char in keyword):
           break
        print("only letters and space is allowed !")
    

    results = [ item for item in books if keyword in  item["name"].lower()]
     
    if results:
       for item in results:
         print(f"-{item['name']} | author: {item['author']} | price: {item['price']:,} uzs")
    else:
         print("book not found")
                
def main():
    books = load_books()
    while True:
        print("welcome to our online store")
        print("-- Add book --")
        print("-- search book --")
        print("-- exit --")

        choice = input("choose 1-3: ").strip()
        if choice == "1":
            add_book(books)
        elif choice == "2":
            search_book(books)
        
        elif choice == "3":
            print("Goodbye !")
            break
        else:
            print("invalid input ! please enter only 1, 2 or 3")
            choice = input("choose 1-3: ").strip()

main()        