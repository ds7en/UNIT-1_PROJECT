import os
from cli_view import commandLine
from login import loginManager
from employee import employees_list, Employee


class Manager:
    def __init__(self, user: str, password: str) -> None:
        self.__user = user
        self.__password = password

    def getUser(self):
        return self.__user

    def getPassword(self):
        return self.__password


manager1 = Manager('ahmed', '1234')


def managerView(result: str) -> str:
    while result == 'm':
        os.system('clear')
        print(f"\n\t\tManager Login \n\n")
        manager_login = loginManager(
            manager1.getUser(), manager1.getPassword())
        if manager_login == True:
            manager = 'main'
            while manager == 'main':
                manager = commandLine(f'Welcome manager, {manager1.getUser().upper()}\n\n\tType one of these commands:\n \t\t (LIST) - List employees\n \t\t (ADD)  - Add new employee\n\t\t (EDIT) - Edit an employee\n \t\t (E)    - Evaluate an employee\n \t\t (HOME) - Logout')
                if manager == 'list':
                    list_view: str = 'list_view'
                    while list_view == 'list_view':
                        os.system('clear')
                        print('\n\t\tEmployees List\n\n\t#   NAME                Evaluate    Employee Role    Employee ID\n\t-   ----                --------    -------------    -----------\n')
                        the_number: int = 0
                        for employee in employees_list:
                            the_number += 1
                            while len(employee.name) < 20:
                                employee.name += ' '
                            while len(employee.role) < 15:
                                employee.role += ' '
                            print(f'\t{the_number}   {employee.name}{employee.evaluate}         {employee.role}  {employee.employee_id}')
                        list_view = input('\nType (BACK) to return to manager window\n > ')
                        if list_view == 'back':
                            manager = 'main'
                        else:
                            list_view = 'list_view'
                    manager = 'main'
                elif manager == 'edit':
                    edit_view: str = 'edit_view'
                    while edit_view == 'edit_view':
                        os.system('clear')
                        print('\n\tChoose one of the employees to edit.\n\n\t#   NAME                          Employee Role\n\t-   ----                          -------------\n')
                        the_number: int = 0
                        for employee in employees_list:
                            the_number += 1
                            while len(employee.name) < 30:
                                employee.name += ' '
                            print(f'\t{the_number}   {employee.name}{employee.role}')
                        the_employee_number = input('\n\t(#) - Insert employee number to edit.\n\t(BACK) - Return to manager window.\n > ')
                        if isinstance(the_employee_number, str) and the_employee_number == 'back':
                            edit_view = 'back'
                        elif int(the_employee_number) <= len(employees_list):
                            the_employee_number = int(the_employee_number)
                            os.system('clear')
                            print('\n\t\tWhat to edit? \n\n\n\t#   NAME                          Employee Role\n\t-   ----                          -------------\n')
                            print(f'\t{the_employee_number}   {employees_list[the_employee_number - 1].name}{employees_list[the_employee_number - 1].role}')
                            edit_command = input('\n\tType one of these commands: \n\t(N) - Edit name.\n\t(R) - Edit employee role\n > ')
                            if edit_command == 'n':
                                os.system('clear')
                                print(f'\n\t\t Change the name of {employees_list[the_employee_number - 1].name}... \n\n')
                                employees_list[the_employee_number - 1].name = input(' New Name: ')
                            elif edit_command == 'r':
                                os.system('clear')
                                print(f'\n\t\t Change the role of {employees_list[the_employee_number - 1].name}... \n\n')
                                employees_list[the_employee_number - 1].role = input(' New Role: ')
                            else:
                                edit_view = 'back'

                        else:
                            edit_view = 'edit_view'

                        if edit_view == 'back':
                            manager = 'main'
                        else:
                            edit_view = 'edit_view'
                elif manager == 'add':
                    add_view: str = 'add_view'
                    while add_view == 'add_view':
                        os.system('clear')
                        print('\n\t\tAdd New Employee')
                        name: str = input('\n Employee Name: ')
                        role: str = input('\n Employee Role: ')
                        evaluate: float = 0.0
                        employee_id = employees_list[-1].employee_id + 1
                        user: str = input('\n Employee Username: ')
                        password: str = input('\n Employee Password: ')
                        new_employee = Employee(
                            name, role, evaluate, employee_id, user, password, complaints=[''])
                        employees_list.append(new_employee)
                        break
                    manager = 'main'
                elif manager == 'e':
                    commandLine('Evaluate an employee')
                    manager = 'main'
                elif manager == 'home':
                    result = 'home'
                else:
                    manager = 'main'
        else:
            os.system('clear')
            login = commandLine("\n\t\tManager Login \n\n\tUsername or password not correct\n\tTry again or back to main?\n")
            if login == 'try':
                result = 'm'
            else:
                result = 'home'
    return result
