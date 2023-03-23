import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="manavin03",
  database="BigMarket"
)
Cursor = db.cursor()

while True:
    print("""
    Welcome To BigMart
    1) Enter as User
    2) Enter as retailer
    3) Enter as Admin
    """)
    x1=int(input())
    user=None
    
    if(x1==1):
        print("""
        1)Register
        2)Login
        """)
        x2=int(input())
        if(x2==1):
            pass
        elif(x2==2):
            user=input()
            password=input()
            Cursor.execute("SELECT * FROM USER WHERE USERNAME='{}' AND PASSWORD='{}';".format(user,password))
            user = Cursor.fetchall()[0]
            if(user==[]):
                print("Invalid credentials")
                continue
            print("You are Succesfully logged in")
            while True:
                print("""
                Welcome {} to BigMart,
                1)Check Top Products
                2)Search Products By Category
                3)Add Product to Cart
                4)Go to Cart
                5)Checkout
                6)LogOut
                """.format(user[0]))
                x3=int(input())
                if(x3==1):
                    #Query for top 10 products
                    pass
                elif(x3==2):
                    #Query to return top 10 products of the category
                    pass
                elif(x3==3):
                    #Query to Add product to cart_product
                    pass
                elif(x3==4):
                    #Query to get products from cart_product of the customer
                    Cursor.execute("select products.ProductName,products.Category,Products.stock,products. Price,products.description,Cart_Product.Quantity,Cart_Product.C artID from Cart_Product join products on products.ProductID=Cart_Product.ProductID where Cart_Product.CartID='{}';".format(user[0]))
                    cart=Cursor.fetchall()
                    if(cart==[]):
                        print("Cart is empty,start shopping now")
                    else:
                        for i in cart:
                            print(cart)
                    
                elif(x3==5):
                    #Query to show cart and total cost 
                    Cursor.execute("select products.ProductName,products.Category,Products.stock,products.Price,products.description,Cart_Product.Quantity,Cart_Product.CartID from Cart_Product join products on products.ProductID=Cart_Product.ProductID where Cart_Product.CartID='{}';".format(user[0]))
                    cart=Cursor.fetchall()
                    if(cart==[]):
                        print("Cart is empty,start shopping now")
                        continue
                    else:
                        val=0
                        for i in cart:
                            print(cart)
                            val+=cart[3]*cart[5]
                        print(val,"Total cost ")
                        
                    print("""
                    Place The order?(y/n)
                    """)
                    s=input()
                    if(s.lower()=="y"):
                        #Query to place order
                        pass
                    elif(s.lower()=="n"):
                        print("Returning to previous screen")
                    else:
                        print("invalid arguments")
                elif(x3==6):
                    user=None
                    break
                else:
                    print("Invalid Arguments")
                    break
        else:
            print("Invalid Arguments")
    elif(x1==2):
        print("""
        1)Register as retailer
        2)Login as retailer
        """)
        x5=int(input())
        if(x5==1):
            pass
        elif(x5==2):
            user=input()
            password=input()
            Cursor.execute("SELECT * FROM USER WHERE USERNAME='{}' AND PASSWORD='{}';".format(user,password))
            user = Cursor.fetchall()[0]
            if(user==[]):
                print("Invalid credentials")
                continue
            print("You are Succesfully logged in")
            while True:
                print("""
                1)Add products to catalogue
                2)Update products in catalogue
                3)Remove products from catalogue
                4)Check catalogue
                5)Check stats
                6)Check Reviews and grievances against products
                7)logout
                """)
                x6=int(input())
                if(x6==1):
                    #Query to insert into products
                    pass
                elif(x6==2):
                    #Query to update products
                    pass
                elif(x6==3):
                    #Query to delete products
                    pass
                elif(x6==4):
                    #Query to look at products
                    pass
                elif(x6==5):
                    print("""
                    1)Look at earnings
                    2)Look at most popular products youve sold
                    3)Look at most profitable categories
                    4)Look at revenue per year
                    
                    """)
                    x7=int(input())
                    
                    if(x7==1):
                        #Query to get total earnings
                        pass
                    elif(x7==2):
                        #Query to check most popular products sold by retailer
                        pass
                    elif(x7==3):
                        #Query to check most popular category for retailer
                        pass
                    elif(x7==4):
                        #olap
                        pass
                    else:
                        print("Invalid Arguments")

                elif(x6==6):
                    print("""
                    1)Check Reviews
                    2)Check Grievances
                    """)
                    x8=int(input())
                    if(x8==1):
                        #Query to get reviews
                        pass
                    elif(x8==2):
                        #Query to get grievances
                        pass
                    else:
                        print("Invalid arguments")
                elif(x6==7):
                    user=None
                    break
                else:
                    print("Invalid Arguments")
                    break

        else:
            print("Invalid Arguments")
            
    elif(x1==3):
        print("""
        Enter Admin Credentials
        """)
        name=input()
        password=input()
    else:
        print("Invalid Arguments")
        

