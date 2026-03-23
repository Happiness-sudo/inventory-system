import requests

BASE = "http://127.0.0.1:5000"

while True:
    print("\n1. Show items")
    print("2. Add item")
    print("3. Update item")
    print("4. Delete item")
    print("5. Fetch product (barcode)")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        res = requests.get(BASE + "/items")
        print(res.json())

    elif choice == "2":
        name = input("Name: ")
        brand = input("Brand: ")

        res = requests.post(BASE + "/items", json={
            "name": name,
            "brand": brand
        })

        print(res.json())

    elif choice == "3":
        item_id = input("ID: ")
        name = input("New name: ")
        brand = input("New brand: ")

        res = requests.patch(BASE + "/items/" + item_id, json={
            "name": name,
            "brand": brand
        })

        print(res.json())

    elif choice == "4":
        item_id = input("ID: ")
        res = requests.delete(BASE + "/items/" + item_id)
        print(res.json())

    elif choice == "5":
        barcode = input("Barcode: ")
        res = requests.get(BASE + "/fetch/" + barcode)
        print(res.json())

    elif choice == "6":
        break