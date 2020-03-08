
from django.shortcuts import render ,redirect 
from django.contrib import messages
from django.contrib.auth.models import auth 
from .models import User 
#from .pyrebase_set import db,auth1 
# Create your views here.

def register(request) :
    if request.method =='POST' :
        #first_name=request.POST['first_name']
        #last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cnf_pass=request.POST['cnf_pass']
        
        if password == cnf_pass  :

          if User.objects.filter(username=username).exists() :
              messages.info(request,'username Taken ')
              return redirect('Humrahi:register')
          elif User.objects.filter(email=email).exists() :
              messages.info(request,'email taken ')
              
              return redirect('Humrahi:register')
            
          else :
            #user =auth.create_user_with_email_and_password(email=email,password=password)
            user=User.objects.create_user(username=username,email=email,password=password)
    
            ##data={
                  #"name":first_name+last_name,
                  #"status":"1"
            #}
            #db.child("users").child(uid).child("details").set(data)
            user.save()
            messages.info(request,'user created ')
            return redirect('Humrahi:login')
        else :
            messages.info(request,"password not matching ")
            return redirect('Humrahi:register')
    else :
        return render(request,'register.html')


def login(request) :
    if request.method=="POST" :
        password=request.POST['password']
        username=request.POST['username']
        user =auth.authenticate(password =password,username=username )
        #user=auth1.sign_in_with_email_and_password(email,password)

        if user is None :
           messages.info(request,"invalid credentials")
           return redirect('Humrahi:login')
        else :
            #session_id=user['idToken']
            #request.session['uid']=str(session_id)
            auth.login(request,user)
            return redirect('/')
    else :
        return render(request,'login.html')

def logout(request)  :
    auth.logout(request) 
    return redirect ('/')



# Create your views here.

def index(request):
    return render(request,'index.html')
