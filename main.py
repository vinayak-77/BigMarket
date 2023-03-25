import mysql.connector
import uuid

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vinayak457",
  database="BigMarket"
)
Cursor = db.cursor()

while True:
    print("""
    Welcome To BigMart
    1) Enter as User
    2) Enter as retailer
    3) Enter as Admin
    4) Exit
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
            try:
                print("Enter a unique username: ")
                username=input()
                print("Enter your email address: ")
                email =input()
                print("Create you password:")
                password = input()
                print("Enter your phone number:")
                pnum = input()
                print("Enter your first name:")
                fname = input()
                print("Enter your middle name:")
                mname = input()
                print("Enter you last name:")
                lname = input()
                print("Enter your Address:")
                address = input()
                print("Enter your zip code:")
                zip_c = input()
                print("Enter you city:")
                city = input()
                Cursor.execute("INSERT INTO USER VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(username,email,password,pnum,fname,mname,lname,address,zip_c,city))
                db.commit()
                customerid = uuid.uuid1()
                past_orders="None"
                Cursor.execute("INSERT INTO CUSTOMER VALUES('{}','{}','{}');".format(customerid,past_orders,username));
                db.commit()
            except:
                print("Username is already taken")
            
        elif(x2==2):
            print("Enter your Username: ")
            user=input()
            print("Enter your Password: ")
            password=input()
            Cursor.execute("SELECT * FROM USER WHERE USERNAME='{}' AND PASSWORD='{}';".format(user,password))
            user = Cursor.fetchall()[0]
            if(user==[]):
                print("Invalid credentials")
                continue
            Cursor.execute("SELECT * FROM CUSTOMER WHERE USERNAME='{}';".format(user[0]))
            Customer=Cursor.fetchall()[0]
            cid = Customer[0]

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
                    #Query to return popular products of the category
                    print("Enter the category you want to search for: ")
                    category = input()
                    Cursor.execute("SELECT Products.ProductID,PRODUCTS.ProductName,Count(Products.ProductID) as Frequency FROM PRODUCTS JOIN ORDER_PRODUCT ON PRODUCTS.ProductID = ORDER_PRODUCT.ProductID JOIN Orders ON ORDERS.OrderID=ORDER_PRODUCT.OrderID JOIN Category ON PRODUCTS.CategoryID=Category.CategoryID WHERE Category.CategoryName='{}' GROUP BY Products.ProductID,Products.ProductName ORDER BY Frequency desc;".format(category))
                    products = Cursor.fetchall()
                    for i in products:
                        print(i)
                elif(x3==3):
                    #Query to Add product to cart_product
                    print("Enter a Product ID: ")
                    product_id = input()
                    print("Enter the quantity: ")
                    qty = int(input())
                    try:
                        Cursor.execute("insert into cart_product values('{}','{}','{}');".format(cid,product_id,qty))
                    except:
                        print("PRODUCT OUT OF STOCK!!!!")
                elif(x3==4):
                    #Query to get products from cart_product of the customer
                    Cursor.execute("select products.ProductName,products.Category,Products.stock,products. Price,products.description,Cart_Product.Quantity,Cart_Product.CartID from Cart_Product join products on products.ProductID=Cart_Product.ProductID where Cart_Product.CartID='{}';".format(cid))
                    cart=Cursor.fetchall()
                    
                    if(cart==[]):
                        print("Cart is empty,start shopping now")
                    else:
                        for i in cart:
                            print(i)
                    
                elif(x3==5):
                    #Query to show cart and total cost 
                    Cursor.execute("select products.ProductName,products.Category,Products.stock,products.Price,products.description,Cart_Product.Quantity,Cart_Product.CartID,Cart_Product.Productid from Cart_Product join products on products.ProductID=Cart_Product.ProductID where Cart_Product.CartID='{}';".format(cid))
                    cart=Cursor.fetchall()
                    if(cart==[]):
                        print("Cart is empty,start shopping now")
                        continue
                    else:
                        val=0
                        for i in cart:
                            print(i)
                            val+=i[3]*i[5]
                        print("Total cost: ",val)
                        
                    print("""
                    Place The order?(y/n)
                    """)
                    s=input()
                    if(s.lower()=="y"):
                        #Query to place order
                        for i in cart:
                            orderid = uuid.uuid1()
                            date='2022-12-04 00:00:00'
                            remarks="None"
                            Cursor.execute("select retailerid from products where productid='{}';".format(i[7]))
                            retailerid = Cursor.fetchall()[0][0]
                            
                            Cursor.execute("insert into orders values('{}','{}','{}','{}','{}');".format(orderid,remarks,date,cid,retailerid))
                            db.commit()
                            Cursor.execute("insert into order_product values('{}','{}');".format(orderid,i[7]))
                            db.commit()
                        
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
            try:
                print("Enter a unique username: ")
                username=input()
                print("Enter your email address: ")
                email =input()
                print("Create you password:")
                password = input()
                print("Enter your phone number:")
                pnum = input()
                print("Enter your first name:")
                fname = input()
                print("Enter your middle name:")
                mname = input()
                print("Enter you last name:")
                lname = input()
                print("Enter your Address:")
                address = input()
                print("Enter your zip code:")
                zip_c = input()
                print("Enter you city:")
                city = input()
                Cursor.execute("INSERT INTO USER VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(username,email,password,pnum,fname,mname,lname,address,zip_c,city))
                db.commit()
                retailerrid = uuid.uuid1()
                
                Cursor.execute("INSERT INTO RETAILER VALUES('{}','{}','{}','{}');".format(retailerrid,0,username,NULL));
                db.commit()
            except:
                print("Username is already taken")
        elif(x5==2):
            print("Enter your Username:")
            user=input()
            print("Enter your password:")
            password=input()
            Cursor.execute("SELECT * FROM USER WHERE USERNAME='{}' AND PASSWORD='{}';".format(user,password))
            user = Cursor.fetchall()[0]
            if(user==[]):
                print("Invalid credentials")
                continue
            Cursor.execute("SELECT * FROM RETAILER WHERE USERNAME='{}';".format(user[0]))
            retailer=Cursor.fetchall()[0]
            rid = retailer[0]
            print("You are Succesfully logged in")
            while True:
                print("""
                1)Add products to catalogue
                2)Update products in catalogue
                3)Remove products from catalogue
                4)Check catalogue
                5)Check stats
                6)logout
                """)
                x6=int(input())
                if(x6==1):
                    #Query to insert into products
                    productid = uuid.uuid1()
                    print("Enter the name of the product:")
                    product = input()
                    print("Enter the product's category:")
                    category = input()
                    print("Enter the stock:")
                    stock = int(input())
                    print("Enter the price:")
                    price = int(input())
                    print("Enter the description:")
                    description=input()
                    Cursor.execute("SELECT CATEGORYID FROM CATEGORY WHERE CATEGORYNAME='{}';".format(category))
                    categoryid = Cursor.fetchall()[0][0]
                    Cursor.execute("INSERT INTO PRODUCTS VALUES('{}','{}','{}','{}','{}','{}','82c0c560-09bb-4044-b865-d2e166f2c932','{}','{}');".format(productid,product,category,stock,price,description,categoryid,rid))
                    db.commit()
                    
                elif(x6==2):
                    #Query to update products
                    pass
                elif(x6==3):
                    #Query to delete products
                    pass
                elif(x6==4):
                    #Query to look at products
                    
                    Cursor.execute("select * from products where retailerid='{}';".format(rid))
                    products=Cursor.fetchall()
                    for i in products:
                        print(i)
                elif(x6==5):
                    print("""
                    1)Look at earnings
                    2)Look at most popular products youve sold
                    3)Look at most profitable categories
                    4)Look at revenue per year
                    
                    """)
                    x7=int(input())
                    
                    if(x7==1):
                        print(retailer[1])
                    elif(x7==2):
                        #Query to check most popular products sold by retailer
                        Cursor.execute(" select cart_product.productid,products.productname,count(*) from cart_product join products on products.productid=cart_product.productid where cart_product.productid in (select productid from products where retailerid='{}') group by productid limit 10;".format(rid))
                        products=Cursor.fetchall()
                        for i in products:
                            print(i)
                    elif(x7==3):
                        #Query to check most popular category for retailer
                        pass
                    elif(x7==4):
                        #olap
                        Cursor.execute("select year(orders.orderdate),sum(products.price) from retailer join products on retailer.RetailerID=products.RetailerID join order_product on order_product.productid=products.productid join orders on orders.orderid=order_product.orderid where retailer.RetailerID='{}' group by (year(orders.orderdate)) with rollup;".format(rid))
                        data=Cursor.fetchall()
                        print("{:<12} {}".format("Year", "Revenue"))
                        print("-" * 25)
                        for i in data:
                            print("{:<12} {}".format(str(i[0]),str(i[1])))
                    else:
                        print("Invalid Arguments")

                # elif(x6==6):
                #     print("""
                #     1)Check Reviews
                #     2)Check Grievances
                #     """)
                #     x8=int(input())
                #     if(x8==1):
                #         #Query to get reviews
                #         Cursor.execute("SELECT *")
                #         pass
                #     elif(x8==2):
                #         #Query to get grievances
                #         pass
                #     else:
                #         print("Invalid arguments")
                elif(x6==6):
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
        print("Enter the username: ")
        name=input()
        print("Enter the password")
        password=input()
        if(name=="root" and password=="root"):
            print("Logged in as admin")
            print("""
            1)check all the sales of a retailers in each months
            2)get the number of products sold of each category for all retailers
            3)find out the category of products most popular in a city
            """)
            x8=int(input())
            if(x8==1):
                Cursor.execute("select monthname(orders.orderdate),sum(products.price),retailer.retailerid from retailer join products on retailer.RetailerID=products.RetailerID join order_product on order_product.productid=products.productid join orders on orders.orderid=order_product.orderid group by monthname(orders.orderdate),retailer.retailerid with rollup;")
                data=Cursor.fetchall()
                print("{:<12} {:<12} {}".format("Month", "Total Sales", "Retailer"))
                print("-" * 50)
                for i in data:
                    print("{:<12} {:<12} {}".format(str(i[0]),str(i[1]),str(i[2])))
                    
            elif(x8==2):
                Cursor.execute("SELECT retailer.retailerid,category.categoryid, COUNT(DISTINCT products.productid) FROM retailer join products on retailer.retailerid=products.retailerid join category ON products.categoryid =category.categoryid JOIN order_product  ON products.productid = order_product.productid GROUP BY retailer.retailerid, category.categoryid having count(distinct products.productid)>=0;")
                data=Cursor.fetchall()
                print("{:<45} {:<45} {}".format("Retailer", "Category", "Sales"))
                print("-" * 100)
                for i in data:
                    print("{:<45} {:<45} {}".format(str(i[0]),str(i[1]),str(i[2])))
                
            elif(x8==3):
                Cursor.execute("select user.city,category.categoryname,count(distinct order_product.productid) as num_products from user join customer on user.username = customer.username join orders on customer.customerid = orders.cid join order_product on orders.orderid = order_product.orderid join products on order_product.productid = products.productid join category on products.categoryid = category.categoryid group by user.city,category.categoryname with rollup;")
                data=Cursor.fetchall()
                print("{:<30} {:<30} {}".format("City", "Category", "Sales"))
                print("-" * 80)
                for i in data:
                    print("{:<30} {:<30} {}".format(str(i[0]),str(i[1]),str(i[2])))
            else:
                print("Invalid Arguments")
    else:
        break
db.commit()
db.close()
        


