class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days=0, email=None):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=0):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment

# Тест расчета зарплаты по часам
employee1 = EmployeeSalary.get_email("Petr", hours=40)
print(f"{employee1.name}, Email: {employee1.email}. Зарплата: {employee1.salary()}")

# Подготовка к тесту изменения зарплаты
EmployeeSalary.set_hourly_payment(500)

# Тест расчета зарплаты по выходным
# Тест расчета по новой почасовой ставке
employee2 = EmployeeSalary.get_hours("Ivan", rest_days=1)
print(f"{employee2.name} отработал {employee2.hours} часов. Зарплата: {employee2.salary()}")
