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


@allure.title('Получение информации о сотруднике с валидным ID компании')
@allure.story('Получить информацию о сотруднике')
@allure.feature('Employee API')
@allure.severity(allure.severity_level.CRITICAL)
def test_recieve_by_id(sql):
    employee = EmployeeObject()
    employee_id = 11288

    try:
        with allure.step('Получить информацию о сотрудниках из API по ID'):
            allure.attach(name='Employee ID', body=str(employee_id), attachment_type=allure.attachment_type.TEXT)
            api_result = employee.get_employee_by_id(employee_id)
            allure.attach(name='API Request', body=f'GET /employee/employeeId={employee_id}', attachment_type=allure.attachment_type.TEXT)
            allure.attach(name='API Response', body=serialize_data(api_result), attachment_type=allure.attachment_type.JSON)
        
        
        with allure.step('Получить информацию о сотруднике по IP из БД'):
            db_result = sql.get_by_id(employee_id)
            allure.attach(name='Database Query', body=f'SELECT * FROM employee WHERE employee_id={employee_id}', attachment_type=allure.attachment_type.TEXT)
            allure.attach(name='Database Result', body=serialize_data(db_result), attachment_type=allure.attachment_type.JSON)
    

        with allure.step('Сравнить результаты из API и БД'):
            assert employee_id is not None
            assert employee.check_status_is(200)
            print(api_result)
            print(db_result)

    
    except Exception as e:
        print(f"Ошибка при выполнении теста: {e}")
        allure.attach(name='Error', body=str(e), attachment_type=allure.attachment_type.TEXT)
        raise

    with allure.step('Результаты Log'):
        api_result_json = serialize_data(api_result)
        db_result_json = serialize_data(db_result)

        allure.attach(name='API Result', body=api_result_json, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='Database Result', body=db_result_json, attachment_type=allure.attachment_type.JSON)


@allure.title('Получения информации о сотрудниках без указания идентификатора компании')
@allure.story('Обработка ошибок при получении информации о сотрудниках')
@allure.feature('Employee API')
@allure.severity(allure.severity_level.CRITICAL)
def test_empty_id(sql):
    employee = EmployeeObject()
    employee_id = None

    try:
        with allure.step('Попытаться получить информацию о сотрудниках из API'):
            allure.attach(name='Employee ID', body=str(employee_id), attachment_type=allure.attachment_type.TEXT)
            api_result = employee.get_employee_by_id(employee_id)
            allure.attach(name='API Request', body=f'GET /employee/employeeId={employee_id}', attachment_type=allure.attachment_type.TEXT)
            allure.attach(name='API Response', body=serialize_data(api_result), attachment_type=allure.attachment_type.JSON)       
        
        with allure.step('Попытаться получить информацию о сотрудниках из БД'):
            db_result = sql.get_by_id(employee_id)
            allure.attach(name='Database Query', body=f'SELECT * FROM employee WHERE employee_id={employee_id}', attachment_type=allure.attachment_type.TEXT)
            allure.attach(name='Database Result', body=serialize_data(db_result), attachment_type=allure.attachment_type.JSON)
    

        with allure.step('Проверить код состояния ответа API и результат БД'):
            assert employee.check_status_is(500)
            assert db_result == []
            print(api_result)
            print(db_result)


    except Exception as e:
        print(f"Ошибка при выполнении теста: {e}")
        allure.attach(name='Error', body=str(e), attachment_type=allure.attachment_type.TEXT)
        raise

    with allure.step('Результаты Log'):
        api_result_json = serialize_data(api_result)
        db_result_json = serialize_data(db_result)

        allure.attach(name='API Result', body=api_result_json, attachment_type=allure.attachment_type.JSON)
        allure.attach(name='Database Result', body=db_result_json, attachment_type=allure.attachment_type.JSON)

