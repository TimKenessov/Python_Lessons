from sqlalchemy import create_engine, inspect
from sqlalchemy import create_engine, text


class DataBase():
    def __init__(self, db_server):
        self.db = create_engine(db_server)
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = self.db.connect()
        return self.connection

    def select_from_employee(self, company_id):
        with self.connect() as connection:
            sql = text('select * from employee where company_id = :company_id')
            return connection.execute(sql, {'company_id': company_id}).mappings().all()

    def insert_employee(self, first_name, last_name, middle_name, company_id, email, url, phone, birthdate, is_active):
        with self.connect() as connection:
            sql = text('''
                insert into employee (first_name, last_name, middle_name, company_id, email, avatar_url, phone, birthdate, is_active)
                values (:first_name, :last_name, :middle_name, :company_id, :email, :url, :phone, :birthdate, :is_active)
            ''')
            connection.execute(sql, {
                'first_name': first_name,
                'last_name': last_name,
                'middle_name': middle_name,
                'company_id': company_id,
                'email': email,
                'url': url,
                'phone': phone,
                'birthdate': birthdate,
                'is_active': is_active
            })
            connection.commit()

    def update_employee(self, employee_id, last_name, email, url, phone, is_active):
        with self.connect() as connection:
            sql = text('''
                       update employee
                       set last_name = :last_name, 
                           email = :email, 
                           avatar_url = :url, 
                           phone = :phone, 
                           is_active = :is_active 
                       where id = :employee_id
                       ''')
            connection.execute(sql, {
                'employee_id': employee_id,
                'last_name': last_name,
                'email': email,
                'url': url,
                'phone': phone,
                'is_active': is_active
            })
            connection.commit()

    def get_by_id(self, employee_id):
        with self.connect() as connection:
            sql = text('select * from employee where id = :id')
            return connection.execute(sql, {'id': employee_id}).mappings().all()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
