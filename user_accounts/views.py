from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from . models import Customers

from django.contrib.auth import authenticate,login as authlogin,logout as authlogout

from rest_framework.authtoken.models import Token

from django.contrib import messages

from rest_framework.authentication import TokenAuthentication

from rest_framework.decorators import authentication_classes

from uberlike.models import Location,VehicleStand

# Create your views here

@authentication_classes([TokenAuthentication])
def signup(request):
    context={}
    v_count = 0
    p_count = 0
    if request.POST and 'plogin' in request.POST:
        """
        <QueryDict: {'csrfmiddlewaretoken': ['BxYeLuUjOKWzevDo2aRI8Zyha2hx5EpFTFLDKYQxO04q6MqQMdPED3jSIio168ja'],
        'name': [''], 'email': [''], 'address': [''], 'phonenumber': [''], 'paswd1': [''], 'paswd2': [''], 'plogin': ['']}>

        """
        
        try:
            first_name=request.POST.get('fname')
            last_name=request.POST.get('lname')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phonenumber')
            pswd1=request.POST.get('paswd1')
            pswd2=request.POST.get('paswd2')
            if pswd1==pswd2:
                context['register']=True
                user=User.objects.create_user(username=first_name,first_name=first_name,last_name=last_name,email=email,password=pswd1)
                user.save()
                token=Token.objects.create(user=user)
                token.save()   
                customer=Customers.objects.create(user=user,name=first_name,address=address,phone_number=phone)        
                customer.category="Passenger"          
                customer.save()
                v_count += 1
                messages.success(request,"you are successfully signed up.")
                
            else:
                context['register']=False
                context['pswd']=True
                messages.error(request,"Password doesn't match.")
        except Exception as e:
            messages.error(request,"Invalid Credentials.")


    if request.POST and 'vlogin' in request.POST:
        """
        <QueryDict: {'csrfmiddlewaretoken': ['RPrybHsYSgbQh8rqUMXzh0SzHQgVZQlN9XeXabocSwjH9peSEPVvM4Daf6np0kfi'], 
        'name': [''], 'email': [''], 'address': [''], 'phonenumber': [''], 'stndname': [''], 'vnumber': [''],
        'pass1': [''], 'pass2': [''], 'vlogin': ['']}>

        """
        
        try:
            first_name=request.POST.get('fname')
            last_name=request.POST.get('lname')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phonenumber')
            stnd_name=request.POST.get('stndname')
            vnumber=request.POST.get('vnumber')
            pswd1=request.POST.get('pass1')
            pswd2=request.POST.get('pass2')
            if pswd1==pswd2:
                context['register']=True
                user=User.objects.create_user(username=first_name,first_name=first_name,last_name=last_name,email=email,password=pswd1)
                user.save()
                token=Token.objects.create(user=user)
                token.save()
                customer=Customers.objects.create(name=first_name,address=address,phone_number=phone,user=user,stand_name=stnd_name,vehicle_number=vnumber)
                customer.category="Vehicle"
                customer.save()
                p_count += 1
                messages.success(request,"you have successfully signed up!")
                
            else:
                context['register']=False
                context['pswd']=False
                messages.error(request,"Password doesn't match.")
        except Exception as e:
            messages.error(request,"Invalid Credentials.")
   
    if request.POST and 'login' in request.POST:
        username=request.POST.get('name')
        password=request.POST.get('pass')
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials!!")

        
    return render(request,'register_login.html',context)

def logout(request):
    authlogout(request)
    return redirect('login')

