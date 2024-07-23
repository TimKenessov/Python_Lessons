from pages.change_info import ChangeInfo
from faker import Faker
from datetime import datetime, date
import json
import allure

fake = Faker()


def serialize_data(data):
    try:
        return json.dumps(data, default=custom_serializer, indent=4)
    except TypeError as e:
        return str(data)

def custom_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


@allure.epic('Employee')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Изменение информации о сотруднике по ID')
@allure.story('Изменить информацию о сотруднике')
@allure.feature('Employee API')  
def test_edit_info(sql):
    change_info = ChangeInfo()
    employee_id = 11288
    payload = {
        "lastName": fake.name(),
        "email": fake.email(),
        "url": "string",
        "phone": fake.basic_phone_number(),
        "isActive": True
    }


    with allure.step('Получить токен для аутентификации'):
        change_info.get_token()


    with allure.step('Отправить запрос на редактирование информации о сотруднике'):
         allure.attach(name='Employee info', body=json.dumps({"employee_id": employee_id, "payload": payload}, indent=4), attachment_type=allure.attachment_type.JSON)
         api_result = change_info.edit_info(employee_id, payload)
         allure.attach(name='API Request', body=f'PATCH/employee/employeeId = {employee_id}, {payload}', attachment_type=allure.attachment_type.JSON)
         allure.attach(name='API Response', body=serialize_data(api_result), attachment_type=allure.attachment_type.JSON)

    
    
    with allure.step('Обновить данные сотрудника в БД'):
        db_result = sql.update_employee(
        employee_id=employee_id,
        last_name=payload["lastName"],
        email=payload["email"],
        url=payload["url"],
        phone=payload["phone"],
        is_active=payload["isActive"]
    )
        allure.attach(name='Database Query', body=f'UPDATE employee where id = {employee_id}', attachment_type=allure.attachment_type.TEXT)
        allure.attach(name='Database Result', body=serialize_data(db_result), attachment_type=allure.attachment_type.JSON)
        

    with allure.step('Проверить статус ответа API и результаты'):
        assert change_info.check_status_is(200)


    with allure.step('Результаты Log'):
        payload_json = serialize_data(payload)
        api_result_text = serialize_data(api_result)
        db_result_text = serialize_data(db_result)

        allure.attach(name='Payload', body=payload_json, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='API Result', body=api_result_text, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='Database Result', body=db_result_text, attachment_type=allure.attachment_type.JSON)
    
    
    print(api_result)
    print(db_result)


@allure.epic('Employee')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Попытаться изменить информацую о сотруднике с пустым ID')
@allure.story('Попытка отправки запроса с невалидными значениями')
@allure.feature('Employee API')  
def test_empty_id(sql):
    change_info = ChangeInfo()
    employee_id = None
    payload = {
        "lastName": fake.last_name(),
        "email": fake.email(),
        "url": "string",
        "phone": fake.basic_phone_number(),
        "isActive": True
        }
    

    with allure.step('Получить токен для аутентификации'):
        change_info.get_token()
    

    with allure.step('Отправить запрос на редактирование информации о сотруднике с пустым ID'):
        api_result = change_info.edit_info(employee_id, payload)


    with allure.step('Попытаться обновить данные сотрудника в БД'):  
        try:
            db_result = sql.update_employee(None, None, None, None, None, None, None, None)
        except TypeError:
            db_result = []
    
    
    with allure.step('Проверить код состояния ответа API и результаты'):
        assert change_info.check_status_is(404)
        assert db_result == []
    
    
    with allure.step('Результаты Log'):
        payload_json = serialize_data(payload)
        api_result_text = serialize_data(api_result)
        db_result_text = serialize_data(db_result)

        allure.attach(name='Payload', body=payload_json, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='API Result', body=api_result_text, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='Database Result', body=db_result_text, attachment_type=allure.attachment_type.JSON)
    
    
    print(api_result)
    print(db_result)


@allure.epic('Employee')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Попытаться изменить информацую о сотруднике с пустым Payload')
@allure.story('Попытка отправки запроса с невалидными значениями')
@allure.feature('Employee API')  
def test_empty_payload(sql):
    change_info = ChangeInfo()
    employee_id = 11288
    payload = None

    
    with allure.step('Получить токен для аутентификации'):
        change_info.get_token()

    
    with allure.step('Отправить запрос на редактирование информации о сотруднике с пустым Payload'):
        api_result = change_info.edit_info(employee_id, payload)


    with allure.step('Попытаться обновить данные сотрудника в БД'):
        try:
            db_result = sql.update_employee(None, None, None, None, None, None, None, None)
        except TypeError:
            db_result = []


    with allure.step('Проверить код состояния ответа API и результаты'):
        assert change_info.check_status_is(401)
        assert db_result == []
    

    with allure.step('Результаты Log'):
        payload_json = serialize_data(payload)
        api_result_text = serialize_data(api_result)
        db_result_text = serialize_data(db_result)

        allure.attach(name='Payload', body=payload_json, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='API Result', body=api_result_text, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='Database Result', body=db_result_text, attachment_type=allure.attachment_type.JSON)
    
    
    print(api_result)
    print(db_result)
