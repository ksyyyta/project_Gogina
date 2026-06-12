class Division:
    def __init__(self, last_name, age, office_number):
        self.last_name = last_name
        self.age = age
        self.office_number = office_number

    def show_office_number(self):
        print(f"Кабинет {self.office_number}")

sotrudnik1 = Division("Иванов", 25, 101)
sotrudnik2 = Division("Петров", 30, 102)
sotrudnik3 = Division("Сидоров", 35, 103)
sotrudnik4 = Division("Козлов", 28, 104)
sotrudnik5 = Division("Соколова", 32, 105)

sotrudnik1.show_office_number()
sotrudnik2.show_office_number()
sotrudnik3.show_office_number()
sotrudnik4.show_office_number()
sotrudnik5.show_office_number()