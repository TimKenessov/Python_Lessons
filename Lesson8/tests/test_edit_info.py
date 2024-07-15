from pages.change_info import ChangeInfo


def test_edit_info():
    change_info = ChangeInfo()
    employee_id = 10617
    payload = {
         "lastName": "Алексеев",
         "email": "noizemctrue@gmail.com",
         "url": "string",
         "phone": "+7 (705) 937-99-92",
         "isActive": True
    }
    change_info.get_token()
    result = change_info.edit_info(employee_id, payload)
    assert change_info.check_status_is(200)
    print(result)


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