from django.shortcuts import render
from . models import VehicleStand
from user_accounts.models import Customers
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    if request.POST and 'avialable-status' in request.POST:
       available=request.POST.get('available')
       notavailable=request.POST.get('not-available')
       print("-------------------",request.POST)
       print("-------------------",available)
       print("-------------------",notavailable)
       # values:none,on
    # my lat  vattaparamb: 11.937336446169454, 75.65324167404668  :11.936248278783117, 75.65216104072476
    user=request.user 
    alls=VehicleStand.objects.all()
    stands = []
    center={}
    near_stand=None
    nearby=None
    if request.POST:
      state=request.POST.get("state")
      city=request.POST.get("city")
      village=request.POST.get("village")
      price_range=request.POST.get("price")
      distance_range=request.POST.get("distance")
      vehicle=request.POST.getlist("taxi")
      for i in vehicle:
        if i=="stand": 
          near_stand =alls.get(location=village)
          near=near_stand.near_by
          nearby=alls.get(location=near)
        else:
           pass  
      
      
    if not user.is_superuser:
      
      
      if user.is_authenticated:
        ad=user.user_profile.address
        addre=ad.strip().split(",")
        
        loc=addre[1]
        near_stand =alls.get(location=loc)
        near=near_stand.near_by
        nearby=alls.get(location=near)
        for s in alls:     
          stands.append({"address":s.address,
                          "description":s.description,
                          "price":s.price,
                          "type":s.type,
                          "size":s.size,
                          "position":{"lat":s.lat,"lng":s.lng}})
          if user.user_profile.category=="Vehicle" and s.location in addre:
              center["lat"]=s.lat
              center["lng"]=s.lng 
              center["zoom"]=17
          else:
            center["lat"]=s.lat
            center["lng"]=s.lng 
            center["zoom"]=14 

          
    content={'user':user,"stands":stands,"center":center,"stand":near_stand,"near_stand":nearby}     
    return render(request,'index copy.html',content)

def profile(request):
    if request.POST and 'location_mark' in request.POST:
       state=request.POST.get("state")
       district=request.POST.get("district")
       city=request.POST.get("city")
       location_mark=request.POST.get("location_mark")
       
    if request.POST and 'destination' in request.POST:
       state=request.POST.get("state")
       district=request.POST.get("district")
       city=request.POST.get("city")
       location_mark=request.POST.get("destination")
       
    if request.POST and 'cardholder_name' in request.POST:
       cardholder_name=request.POST.get("cardholder_name")
       card_number=request.POST.get("card_number")
       expire_date=request.POST.get("expire_date")
       card_password=request.POST.get("card_password")
        
    return render(request,'sidebar.html')

def detail(request,slug):
    center={}
    stands=[]
    page=1
    user=request.user
    stand=VehicleStand.objects.get(slug=slug)
    stand_name=stand.location
    vehicles=Customers.objects.all().filter(stand_name=stand_name)
    if request.GET:
       page=request.GET.get('page',1)
    vehicle_paginator=Paginator(vehicles,1)  
    vehicle_page=vehicle_paginator.get_page(page) 
    
    center['lat']=stand.lat
    center['lng']=stand.lng
    stands.append({"address":stand.address,
                          "description":stand.description,
                          "price":stand.price,
                          "type":stand.type,
                          "size":stand.size,
                          "position":{"lat":stand.lat,"lng":stand.lng}})
    context={"stand":stands,"center":center,"std":stand,'stand_vehicles':vehicles,"vehicles":vehicle_page}
    return render(request,'vdetails.html',context)

