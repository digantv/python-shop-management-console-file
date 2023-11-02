import os
from user_management.User import User
from user_management.UserOptions import UserOptions


class UserManagement:
    al = []
    file_path = "C://Users//yash//PycharmProjects//shop_management//user_management//Users.csv"

    @staticmethod
    def user_management():
        can_i_keep_running_the_program = True

        while can_i_keep_running_the_program:
            print("**** Welcome to User Management *****")
            print("\n")
            print("What would you like to do?")
            print("1. Add User")
            print("2. Edit User")
            print("3. Delete User")
            print("4. Search User")
            print("5. Quit")

            option_selected_by_user = int(input())

            if option_selected_by_user == UserOptions.QUIT:
                UserManagement.save_data_to_file()
                print("!!! Program closed")
                can_i_keep_running_the_program = False

            elif option_selected_by_user == UserOptions.ADD_USER:
                UserManagement.add_user()
                print("\n")

            elif option_selected_by_user == UserOptions.SEARCH_USER:
                sn = input("Enter User Name to search: ")
                UserManagement.search_user(sn)
                print("\n")

            elif option_selected_by_user == UserOptions.DELETE_USER:
                delete_user_name = input("Enter User Name to delete: ")
                UserManagement.delete_user(delete_user_name)
                print("\n")

            elif option_selected_by_user == UserOptions.EDIT_USER:
                edit_user_name = input("Enter User Name to edit: ")
                UserManagement.edit_user(edit_user_name)
                print("\n")

    @staticmethod
    def add_user():
        user_object = User()
        user_object.userName = input("User Name: ")
        user_object.loginName = input("Login Name: ")
        user_object.password = input("Password: ")
        user_object.confirmPassword = input("Confirm Password: ")
        user_object.userRole = input("User Role: ")
        UserManagement.al.append(user_object)

    @staticmethod
    def search_user(user_name):
        for user in UserManagement.al:  # Observer List iterator
            if user.userName.lower() == user_name.lower():
                UserManagement.print_user_details(user)
                return
        print("User not found.")

    @staticmethod
    def delete_user(user_name):
        for user in UserManagement.al[:]:
            if user.userName.lower() == user_name.lower():
                UserManagement.al.remove(user)
                print(f"User {user.userName} has been deleted.")
                return
        print("User not found.")

    @staticmethod
    def edit_user(user_name):
        for user in UserManagement.al:
            if user.userName.lower() == user_name.lower():
                UserManagement.print_user_details(user)
                user.userName = input("New User Name: ")
                user.loginName = input("New Login Name: ")
                user.password = input("New Password: ")
                user.confirmPassword = input("New Confirm Password: ")
                user.userRole = input("New User Role: ")
                print("User information updated.")
                return
        print("User not found.")

    @staticmethod
    def print_user_details(user):
        print("User Name: " + user.userName)
        print("Login Name: " + user.loginName)
        print("Password: " + user.password)
        print("User Role: " + user.userRole)

    @staticmethod
    def load_data_from_file():
        if os.path.exists(UserManagement.file_path):
            with open(UserManagement.file_path, "r") as file:
                for line in file:
                    user_data = line.strip().split(",")
                    if len(user_data) > 3:
                        # Parameterised constructor call
                        user = User(user_data[2], user_data[0], user_data[1], "", user_data[3])
                        UserManagement.al.append(user)

    @staticmethod
    def save_data_to_file():
        print("Saving Users data to file")
        with open(UserManagement.file_path, "w") as file:
            for user in UserManagement.al:
                file.write(f"{user.loginName},{user.password},{user.userName},{user.userRole}\n")

    @staticmethod
    def validate_user_and_password(login_name, password):
        UserManagement.load_data_from_file()
        for user in UserManagement.al:
            if user.loginName.lower() == login_name.lower() and user.password == password:
                return True
        return False
