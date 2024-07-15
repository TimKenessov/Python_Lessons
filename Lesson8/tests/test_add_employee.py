from pages.add_employee import NewEmployee
import pytest


def test_add_new():
    new_employee = NewEmployee()
    new_employee.get_token()
    payload = {
  "id": 0,
  "firstName": "Иван",
  "lastName": "Алексеев",
  "middleName": "Noize",
  "companyId": 14732,
  "email": "noizemc@mail.ru",
  "url": "string",
  "phone": "937-99-92",
  "birthdate": "2024-07-10T22:46:28.367Z",
  "isActive": True
}
    result = new_employee.add_new_employee(payload)
    print(result)
    assert new_employee.check_status_is(201)


def test_add_empty():
    new_employee = NewEmployee()
    new_employee.get_token()
    payload = {}
    new_employee.add_new_employee(payload)
    assert new_employee.check_status_is(500)