from django.shortcuts import render
from . models import VehicleStand,LocationSearch
from user_accounts.models import Customers
from django.contrib.auth.models import User
from django.core.paginator import Paginator



# Create your views here.
def home(request):
   if request.POST and 'avialable-status' in request.POST:
      available=request.POST.get('available')
      notavailable=request.POST.get('not-available')  # values:none,on
   user=request.user 
   alls=VehicleStand.objects.all()
   search_count_list = []
   recent_searched_location_list=[]
   stands = []
   center={}
   near_stand=None
   nearby=None
   search_result=None
   if request.POST:
      state=request.POST.get("state")
      district=request.POST.get("city")
      city=request.POST.get("village")
      price_range=request.POST.get("price")
      distance_range=request.POST.get("distance")
      vehicle=request.POST.getlist("taxi")
      search_result=VehicleStand.objects.filter(location=city)
      for j in alls:
         if city == j.location and user.is_authenticated:
            search_location= LocationSearch.objects.get_or_create(id=j.pk,user=user,location=j)
            location_search = LocationSearch.objects.get(location=j)
            location_search.search_count += 1
            location_search.save()
            break
            
      for i in vehicle:
         if i=="stand": 
            near_stand = VehicleStand.objects.get(location=city)
            # near_stand = VehicleStand.objects.filter(district=district)
            near=near_stand.near_by
            nearby = VehicleStand.objects.get(location=near)
         else:
            pass  
   if not user.is_superuser:
      if user.is_authenticated:
         # nearby stands in your district,it can be change to city
         ad=user.user_profile.address
         addre=ad.strip().split(",")  
         loc=addre[3]  # here loc is the district of the user
         near_stand = VehicleStand.objects.filter(district=loc)
         #   near=near_stand.near_by
         #   nearby=VehicleStand.objects.get(location=near)
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
   if user.is_authenticated:            
      # most searched location list using search count of the location
      most_serached_location = LocationSearch.objects.order_by('-search_count')
      for count in most_serached_location:
         data=VehicleStand.objects.get(pk=count.pk)
         search_count_list.append(data)

   if user.is_authenticated:
      # recently searched location list using recent updated date
      recently_updated_search_list=LocationSearch.objects.order_by('-updated_at')
      for data in recently_updated_search_list:
         recently_Searched_location=VehicleStand.objects.get(pk=data.location.pk)    
         recent_searched_location_list.append(recently_Searched_location) 

   

   content={'user':user,"stands":stands,"center":center,"stands":near_stand,"search_result":search_result,"most_searched_loc":search_count_list,"recent_searched_location":recent_searched_location_list} 

   return render(request,'index.html',content)

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
    stand_name=stand.name
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

