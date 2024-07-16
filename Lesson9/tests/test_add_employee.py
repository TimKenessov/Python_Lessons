from pages.add_employee import NewEmployee
from pages.data_base import DataBase
from faker import Faker


db_server = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'
database = DataBase(db_server)

fake = Faker()


def test_add_new():
    new_employee = NewEmployee()
    new_employee.get_token()
    payload = {
        "id": 0,
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "middleName": fake.first_name(),
        "companyId": 15809,
        "email": fake.email(),
        "url": "string",
        "phone": fake.basic_phone_number(),
        "birthdate": fake.date_of_birth().isoformat(),
        "isActive": True
    }
    api_result = new_employee.add_new_employee(payload)
    db_result = database.insert_employee(
        first_name=payload["firstName"],
        last_name=payload["lastName"],
        middle_name=payload["middleName"],
        company_id=payload["companyId"],
        email=payload["email"],
        url=payload["url"],
        phone=payload["phone"],
        birthdate=payload["birthdate"],
        is_active=payload["isActive"]
    )
    print(api_result)
    print(db_result)
    assert new_employee.check_status_is(201)


def test_add_empty():
    new_employee = NewEmployee()
    new_employee.get_token()
    payload = {}
    new_employee.add_new_employee(payload)
    assert new_employee.check_status_is(500)
