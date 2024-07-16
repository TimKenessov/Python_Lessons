from pages.get_employee import EmployeeObject
from pages.data_base import DataBase
import pytest


db_server = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'
database = DataBase(db_server)


def test_get_employee():
    employee = EmployeeObject()
    company_id = 15809
    api_result = employee.get_employee(company_id)
    db_result = database.select_from_employee(company_id)
    assert len(api_result) == len(db_result)
    assert employee.check_status_is(200)
    print(api_result)
    print(db_result)


def test_get_employee_without_company():
    employee = EmployeeObject()
    company_id = {}
    result = employee.get_employee(company_id)
    assert not employee.check_status_is(200)
    print(result)
