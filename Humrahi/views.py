
from django.shortcuts import render ,redirect 
from django.contrib import messages
from django.contrib.auth.models import User,auth 

# Create your views here.
def register(request) :
    if request.method =='POST' :
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cnf_pass=request.POST['cnf_pass']
        
        if password == cnf_pass :

          if User.objects.filter(username=username).exists() :
              messages.info(request,'ussername Taken ')
              return redirect('register')
              
          elif User.objects.filter(email=email).exists() :
              messages.info(request,'email taken ')
              
              return redirect('register')
            
          else :
              user =User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name
              )
              user.save()
              messages.info(request,'user created ')
              return redirect('login')
        else :
            messages.info(request,"password not matching ")
            return redirect('register')
    else :
        return render(request,'register.html')


def login(request) :
    if request.method=="POST" :
        password=request.POST['password']
        username=request.POST['username']
        user =auth.authenticate(username =username ,password =password )

        if user is None :
            messages.info(request,"invalid credentiaals")
            return redirect('login')
        else :
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
