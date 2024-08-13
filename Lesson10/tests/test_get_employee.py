from pages.get_employee import EmployeeObject
import allure 
from datetime import datetime, date
import json

def serialize_data(data):
    try:
        return json.dumps(data, default=custom_serializer, indent=4)
    except TypeError as e:
        return str(data)

def custom_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


@allure.title('Получить информацию о сотруднике с валидным ID компании')
@allure.story('Получить информацию о сотруднике')
@allure.feature('Employee API')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_employee(sql):
    employee = EmployeeObject()
    company_id = 15809

    with allure.step('Получить информацию о сотрудниках из API'):
        allure.attach(name='Company ID', body=str(company_id), attachment_type=allure.attachment_type.TEXT)
        api_result = employee.get_employee(company_id)
        allure.attach(name='API Request', body=f'GET /employee/companyId={company_id}', attachment_type=allure.attachment_type.TEXT)
        allure.attach(name='API Response', body=serialize_data(api_result), attachment_type=allure.attachment_type.JSON)
    
    with allure.step('Получить информацию о сотрудниках из БД'):
        db_result = sql.select_from_employee(company_id)
        allure.attach(name='Database Query', body=f'SELECT * FROM employee WHERE company_id={company_id}', attachment_type=allure.attachment_type.TEXT)
        allure.attach(name='Database Result', body=serialize_data(db_result), attachment_type=allure.attachment_type.JSON)

    with allure.step('Сравнить результаты из API и БД'):
        assert len(api_result) == len(db_result)
        assert employee.check_status_is(200)

    with allure.step('Результаты Log'):
        allure.attach(name='API Result JSON', body=serialize_data(api_result), attachment_type=allure.attachment_type.JSON)
        allure.attach(name='Database Result JSON', body=serialize_data(db_result), attachment_type=allure.attachment_type.JSON)

    print(api_result)
    print(db_result)



@allure.title('Получить информации о сотрудниках без указания ID компании')
@allure.story('Обработка ошибок при получении информации о сотрудниках')
@allure.feature('Employee API')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_employee_without_company(sql):
    employee = EmployeeObject()
    company_id = None

    with allure.step('Попытка получить информацию о сотрудниках из API'):
        allure.attach(name='Company ID', body=str(company_id), attachment_type=allure.attachment_type.TEXT)
        api_result = employee.get_employee(company_id)
        allure.attach(name='API Request', body='GET /employee/companyId=None', attachment_type=allure.attachment_type.TEXT)
        allure.attach(name='API Response', body=serialize_data(api_result), attachment_type=allure.attachment_type.JSON)
    
    with allure.step('Попытка получить информацию о сотрудниках из БД'):
        db_result = sql.select_from_employee(company_id)
        allure.attach(name='Database Query', body='SELECT * FROM employee WHERE company_id=None', attachment_type=allure.attachment_type.TEXT)
        allure.attach(name='Database Result', body=serialize_data(db_result), attachment_type=allure.attachment_type.JSON)

    with allure.step('Проверка кода состояния ответа API и результата БД'):
        assert not employee.check_status_is(200)
        assert employee.check_status_is(500)
        assert db_result == []

    with allure.step('Результаты Log'):
        allure.attach(name='API Result JSON', body=serialize_data(api_result), attachment_type=allure.attachment_type.JSON)
        allure.attach(name='Database Result JSON', body=serialize_data(db_result), attachment_type=allure.attachment_type.JSON)

    print(api_result)
    print(db_result)