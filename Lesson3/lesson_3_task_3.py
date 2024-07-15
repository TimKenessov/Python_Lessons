from address import Address
from mailing import Mailing

to_address = Address("123456", "Алматы", "Темерьязева", "134", "28")

from_address = Address("678900", "Астана", "Красина", "49", "228")

mailing = Mailing(to_address, from_address, 500, "NUR228")

print("Отправление", mailing.track, "из", from_address.index, from_address.city, from_address.street, from_address.house, from_address.apartment, "в", to_address.index, to_address.city, to_address.street, to_address.house, to_address.apartment, "Стоимость", mailing.cost, "рублей.")