from product_management.ProductManagement import ProductManagement
from user_management.UserManagement import UserManagement


def main():
    can_i_keep_running_the_program = True

    print("**** Welcome to Shop Management *****")
    print("\n")

    login_name: str = input("Enter login name: ")
    password = input("Enter password: ")

    if not UserManagement.validate_user_and_password(login_name, password):
        print("!!!!!!!! Login failed. Closing the application")
        return

    while can_i_keep_running_the_program:
        print("**** Welcome to Shop Management *****")
        print("\n")

        print("What would you like to do?")
        print("1. User Management")
        print("2. Product Management")
        print("5. Quit")

        option_selected_by_user = int(input())

        if option_selected_by_user == 1:
            UserManagement.user_management()
        elif option_selected_by_user == 2:  # Implement Product Management similar to User Management
            ProductManagement.product_management()
        elif option_selected_by_user == 5:
            break


if __name__ == '__main__':
    main()
