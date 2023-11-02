import os

from product_management.ProductOptions import ProductOptions
from product_management.Product import Product


class ProductManagement:
    al = []
    file_path = "C://Users//yash//PycharmProjects//shop_management//product_management//Products.csv"

    @staticmethod
    def product_management():
        can_i_keep_running_the_program = True
        while can_i_keep_running_the_program:
            print("**** Welcome To Product Management ****")
            print("\n")
            print("What Do Want To Do ? ")
            print("1.Add Product")
            print("2.Edit Product")
            print("3.Delete Product")
            print("4.Search Product")
            print("5.Quit")

            option_selected_by_user = int(input())

            if option_selected_by_user == ProductOptions.QUIT:
                can_i_keep_running_the_program = False
                print("Program Closed!!!!")
                print("\n")
            elif option_selected_by_user == ProductOptions.ADD_PRODUCT:
                ProductManagement.add_product()
                print("\n")
            elif option_selected_by_user == ProductOptions.EDIT_PRODUCT:
                productName = input()
                ProductManagement.edit_product(productName)

    @staticmethod
    def add_product():
        product_object = Product()
        print("Enter Product Details")
        product_object.productName = input("Enter Product Name: ")
        product_object.productID = input("Enter Product ID: ")
        product_object.availableQuantity = input("Enter Product Quantity: ")
        product_object.productPrice = input("Enter Product Price: ")
        product_object.productCategory = input("Enter Product Category: ")
        ProductManagement.al.add(product_object)
        print("Product Added Successfully!!!!")

    @staticmethod
    def edit_product(productName):
        for product in ProductManagement.al:
            if product.productName == productName:
                print(f"Editing Product ", {productName})
                product.productName = input("Enter New Product Name: ")
                product.productID = input("Enter New Product ID: ")
                product.availableQuantity = input("Enter New Available Quantity: ")
                product.productPrice = input("Enter New Product Price: ")
                product.productCategory = input("Enter New Product Category")
                return
            print("User Not Found!!!")

    @staticmethod
    def delete_user(productName):
        for product in ProductManagement.al:
            if product.productName == productName:
                ProductManagement.al.remove(product)
                return
            print("User Not Found!!!")

    @staticmethod
    def search_user(productName):
        for product in ProductManagement.al:
            if product.productName == productName:
                ProductManagement.print_product_details(product)
                return
            print("User Not Found!!!")

    @staticmethod
    def print_product_details(product):
        print("Product Name: " + product.productName)
        print("Product ID: " + product.productID)
        print("Available Quantity: " + product.availableQuantity)
        print("Product Price: " + product.productPrice)
        print("Product Category: " + product.productCategory)

    @staticmethod
    def load_data_from_file():
        if os.path.exists(ProductManagement.file_path):
            with open(ProductManagement.file_path, "r") as file:
                for line in file:
                    product_data = line.strip().split(",")
                    if len(product_data) > 4:
                        # Parameterised constructor call
                        product = Product(product_data[2], product_data[0], product_data[1], "", product_data[3])
                        ProductManagement.al.append(product)

    @staticmethod
    def save_data_to_file():
        print("Saving Product Data to File")
        with open(ProductManagement.file_path, "w") as file:
            for product in ProductManagement.al:
                file.write(f"{product.productName},{product.productID},{product.availableQuantity},"
                           f"{product.productPrice},{product.productCategory}\n")
