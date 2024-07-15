from pages.get_employee import EmployeeObject
import pytest


def test_get_employee():
    employee = EmployeeObject()
    company_id = 14732
    result = employee.get_employee(company_id)
    print(result)
    assert employee.check_status_is(200)


def test_get_employee_without_company():
    employee = EmployeeObject()
    company_id = {}
    result = employee.get_employee(company_id)
    assert not employee.check_status_is(200)
    print(result)
   