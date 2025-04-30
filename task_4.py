
class EmployeeSalary:
    hourly_payment = 400  # зарплата за час работы
    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment

employee = EmployeeSalary.get_hours('Иван', None, 2, None)
employee = EmployeeSalary.get_email(employee.name, employee.hours, employee.rest_days, employee.email)

print(employee.name)         # Иван
print(employee.hours)        # 40 (5 рабочих дней × 8 часов)
print(employee.email)        # Иван@email.com
print(employee.salary())     # 16000 (40 * 400)

# Изменим оплату
EmployeeSalary.set_hourly_payment(500)
print(employee.salary())