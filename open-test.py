import csv
import os
import locale

maxantal = 11

def format_currency(value):
    return locale.currency(value,grouping=True)

def list_products(products):
    for idx, product in enumerate(products, 1):
        print(f"{idx} {product["name"]} {product["price"]}kr på lager:{product["quantity"]}")

def view_product(idx, products):
    product = products[idx -1]
    return product

def load_data(filename): 
    products = []  #lista
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,   
                    "price": price,
                    "quantity": quantity
                })
    return products

#TODO: hur gör man så funktionen load_data returnerar products istället?
#TODO: gör så man kan se en numrerad lista som börjar på 1.
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id

os.system('cls')

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')

while True:
    list_products(products)
    
    idx = int(input("Välj product med nummer"))
    
    product = view_product(idx, products)
    print(f"product: {product["name"]} , {product["desc"]}")
    
    tabort = int(input("ta bort en produkt, skriv produkt nummer:"))
    
    if 1 <= tabort <= maxantal:
        produktbortagen = products.pop(tabort -1) and (maxantal - 1)
    else:
        print("Du måste skriva ett produktnummer som existerar")
    input()
