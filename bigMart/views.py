from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import mysql.connector as sql

@csrf_exempt 
def index(request):
    if(request.method== 'POST'):
        Username=request.POST['Username']
        Email=request.POST['Email']
        Password=request.POST['Password']
        PhoneNumber=request.POST['PhoneNumber']
        Firstname=request.POST['Firstname']
        Middlename=request.POST['Middlename']
        Lastname=request.POST['Lastname']
        Address=request.POST['Address']
        Zip=request.POST['Zip']
        City=request.POST['City']
        connector=sql.connect(host="localhost",user="root",passwd="manavin03",database="BigMarket")
        print(PhoneNumber)
        cursor = connector.cursor()
        cursor.execute("insert into User Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Username,Email,Password,PhoneNumber,Firstname,Middlename,Lastname,Address,Zip,City))
        connector.commit()
    return render(request,"index.html")