from pages.get_employee import EmployeeObject
import pytest


def test_recieve_by_id():
    employee = EmployeeObject()
    employee_id = 10617
    employee_info = employee.get_employee_by_id(employee_id)
    assert employee_id is not None
    assert employee.check_status_is(200)
    print(employee_info)


def test_empty_id():
    employee = EmployeeObject()
    employee_id = {}
    employee_info = employee.get_employee_by_id(employee_id)
    assert employee.check_status_is(500)
    print(employee_info)