from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 14", "+7937999211")
catalog.append(phone1)

phone2 = Smartphone("Samsung", "Galaxy S24 Ultra", "+7937999212")
catalog.append(phone2)

phone3 = Smartphone("Xiaomi", "Poco X6", "+7937999213")
catalog.append(phone3)

phone4 = Smartphone("Motorolla", "L6", "+7937999214")
catalog.append(phone4)

phone5 = Smartphone("Nokia", "N95", "+7937999215")
catalog.append(phone5)

for phone in catalog:
    print(phone.brand, phone.model, phone.phone_number)