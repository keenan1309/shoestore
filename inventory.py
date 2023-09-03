
#========The beginning of the class==========

class Shoe:
    '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
    '''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost
       

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity


    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
        '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
        shoe_inv = open("inventory.txt","r")
        shoes = shoe_inv.readlines()
        for shoe in shoes[1:]:
            shoe_split = shoe.split(",")
            shoe_list.append(Shoe(shoe_split[0], shoe_split[1], shoe_split[2], shoe_split[3], shoe_split[4]))
        shoe_inv.close()


def capture_shoes():
        '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
'''
        shoe_inv = open("inventory.txt","a+")
        user_country = input("Please enter the country of origin : ")
        user_sku = input("Please enter SKU code number no more then 5 digits :")
        user_product = input("Please enter the name of the user product :")
        user_price = float(input("Please enter a price for the shoe being captured : "))
        user_qty = int(input("Please enter the quantity of stock held : "))
        shoe_capt = (f"\n{user_country},SKU{user_sku},{user_product},{user_price},{user_qty}")
        shoe_inv.write(shoe_capt)
        print("Thank you this has been added to the stock list database !!")
        shoe_inv.close()


def re_stock():
        '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
'''
        low_num = int(shoe_list[0].quantity)
        for shoe in shoe_list:
             if int(shoe.quantity) < low_num:
                  low_num = int(shoe.quantity)
                  prod_name = (shoe.product)
        print(f"The product with the lowest quantity - {prod_name} - Qty is :{low_num}")
        re_stock_user_inp = str(input("May you please advise the amount you would like to restock with : "))
        shoe_file = open("inventory.txt","r")
        shoe_qty = shoe_file.read()
        re_stock_amt = shoe_qty.replace(str(low_num),re_stock_user_inp)
        shoe_file.close()
        shoe_file = open("inventory.txt","w")
        shoe_file.write(re_stock_amt)
        print("Thank you the item has been re-stocked !")


def seach_shoe():
        '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
        '''
        sku_input = input("Please can you insert a SKU you would like too search : ")
        for shoe in shoe_list:
             if sku_input == shoe.code:
                print(f"Country - {shoe.country}\nSku Num - {shoe.code}\nProduct - {shoe.product}\nCost - R {shoe.cost}\nQuantity Stock - {shoe.quantity}")


def value_per_item():
        '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
'''
        count = 0
        for i in shoe_list:
             print(f"{count}.{i.product} - {i.code}")
             count += 1
        user_num = int(input("Please input a number for the shoe you would like to view : "))
        tot_cos = float(shoe_list[user_num].cost) * float(shoe_list[user_num].quantity)
        print(f"The total value of the current stock of the shoe {shoe_list[user_num].product} is R {tot_cos}")


def highest_qty():
        '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
        big_num = int(shoe_list[0].quantity)
        for shoe in shoe_list:
             if int(shoe.quantity) > big_num:
                  big_num = int(shoe.quantity)
                  prod_name = (shoe.product)
        print(f"The product with the highest quantity is - {prod_name} - Qty is :{big_num}")
        print(f"Item to please be marked for sale !")


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
'''
    count = 0
    print("Kindly see below list of shoes :")
    for i in shoe_list:
        print(f"{count}.Country - {i.country}, Sku Code - {i.code}, Product type - {i.product}, Cost - {i.cost}, Quantity - {i.quantity}")
        count += 1


#==========Main Menu=============
while True:
    '''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
    menu = int(input('''Greetings! Please select a value below:
    0.Load data
    1.Capture shoe
    2.Re-stock shoe
    3.Search shoe
    4.Value of shoe
    5.Highest Quantity
    6.View All Shoes
    Please input the number selecttion you would like over here : '''))
    #Create loop for the user if data not loaded, using if and else statement.
    if menu == 0:
        print(read_shoes_data())
    if len(shoe_list) != 0:
          
        if menu == 1:
            print(capture_shoes())
            
        if menu == 2:
            print(re_stock())
            
        if menu == 3:
            print(seach_shoe())
            
        if menu == 4:
            print(value_per_item())
            
        if menu == 5:
            print(highest_qty())
            
        if menu == 6:
            print(view_all())
    else:
         print("Pick option 0 to load in data")
         
