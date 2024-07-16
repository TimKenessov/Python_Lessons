from pages.change_info import ChangeInfo
from pages.data_base import DataBase
from faker import Faker


db_server = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'
database = DataBase(db_server)

fake = Faker()


def test_edit_info():
    change_info = ChangeInfo()
    employee_id = 10744
    payload = {
        "lastName": fake.last_name(),
        "email": fake.email(),
        "url": "string",
        "phone": fake.basic_phone_number(),
        "isActive": True
    }
    change_info.get_token()
    api_result = change_info.edit_info(employee_id, payload)
    db_result = database.update_employee(
        employee_id=employee_id,
        last_name=payload["lastName"],
        email=payload["email"],
        url=payload["url"],
        phone=payload["phone"],
        is_active=payload["isActive"]
    )
    assert change_info.check_status_is(200)
    print(api_result)
    print(db_result)


def test_empty_id():
    change_info = ChangeInfo()
    employee_id = {}
    payload = {}
    change_info.get_token()
    result = change_info.edit_info(employee_id, payload)
    assert change_info.check_status_is(500)
    print(result)


def test_empty_payload():
    change_info = ChangeInfo()
    employee_id = {10610}
    payload = {}
    change_info.get_token()
    result = change_info.edit_info(employee_id, payload)
    assert change_info.check_status_is(500)
    print(result)
