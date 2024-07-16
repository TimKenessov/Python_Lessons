from pages.get_employee import EmployeeObject
from pages.data_base import DataBase


db_server = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'
database = DataBase(db_server)


def test_recieve_by_id():
    employee = EmployeeObject()
    employee_id = 10744
    api_result = employee.get_employee_by_id(employee_id)
    db_result = database.get_by_id(employee_id)
    assert employee_id is not None
    assert employee.check_status_is(200)
    print(api_result)
    print(db_result)


def test_empty_id():
    employee = EmployeeObject()
    employee_id = {}
    employee_info = employee.get_employee_by_id(employee_id)
    assert employee.check_status_is(500)
    print(employee_info)
