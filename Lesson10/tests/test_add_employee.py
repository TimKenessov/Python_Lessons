from pages.add_employee import NewEmployee
import allure
import json
from datetime import datetime, date

from faker import Faker


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


@allure.title('Добавление нового сотрудника')
@allure.story('Создание нового сотрудника')
@allure.feature('Employee API')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_new(sql):
    new_employee = NewEmployee()

    
    with allure.step('Получить токен для аутентификации'):
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


    with allure.step('Отправить запрос на добавление нового сотрудника'):
        allure.attach(name='Employee info', body=str(payload), attachment_type=allure.attachment_type.JSON)
        api_result = new_employee.add_new_employee(payload)
        allure.attach(name='API request', body=f'POST/employee, payload = {payload}', attachment_type=allure.attachment_type.JSON)
        allure.attach(name='API Response', body=serialize_data(api_result), attachment_type=allure.attachment_type.JSON)

        
    with allure.step('Вставить данные сотрудника в базу данных'):
        db_result = sql.insert_employee(
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
        allure.attach(name='Database Query', body=f'INSERT INTO employee (first_name, last_name, middle_name, company_id, email, avatar_url, phone, birthdate, is_active)', attachment_type=allure.attachment_type.TEXT)
        allure.attach(name='Database Result', body=serialize_data(db_result), attachment_type=allure.attachment_type.JSON)
    

    with allure.step('Проверить статус ответа API и результаты'):
        assert new_employee.check_status_is(201)
    

    with allure.step('Результаты Log'):
        payload_json = serialize_data(payload)
        api_result_text = serialize_data(api_result)
        db_result_text = serialize_data(db_result)

        allure.attach(name='Payload', body=payload_json, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='API Result', body=api_result_text, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='Database Result', body=db_result_text, attachment_type=allure.attachment_type.JSON)
    

    print(api_result)
    print(db_result)


@allure.title('Попытка добавления сотрудника с пустыми данными')
@allure.story('Обработка ошибок при добавлении сотрудника')
@allure.feature('Employee API')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_empty(sql):
    new_employee = NewEmployee()


    with allure.step('Получить токен для аутентификации'):
        new_employee.get_token()
    payload = None

    with allure.step('Отправить запрос на добавление сотрудника с пустыми данными'):
        api_result = new_employee.add_new_employee(payload)


    try:
        with allure.step('Попытаться вставить пустые данные в базу данных'):
            db_result = sql.insert_employee(None, None, None, None, None, None, None, None)
    except TypeError:
        db_result = []
    

    with allure.step('Проверить код состояния ответа API и результаты'):
        assert new_employee.check_status_is(500)
        assert db_result == []
    

    with allure.step('Результаты Log'):
        payload_json = serialize_data(payload)
        api_result_text = serialize_data(api_result)
        db_result_text = serialize_data(db_result)

        allure.attach(name='Payload', body=payload_json, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='API Result', body=api_result_text, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='Database Result', body=db_result_text, attachment_type=allure.attachment_type.JSON)
    
    
    print(api_result)
    print (db_result)
