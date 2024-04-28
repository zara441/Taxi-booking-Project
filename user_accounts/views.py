from django.shortcuts import render

# Create your views here.
def login(request):
    if request.POST and 'plogin' in request.POST:
        """
        <QueryDict: {'csrfmiddlewaretoken': ['BxYeLuUjOKWzevDo2aRI8Zyha2hx5EpFTFLDKYQxO04q6MqQMdPED3jSIio168ja'],
        'name': [''], 'email': [''], 'address': [''], 'phonenumber': [''], 'paswd1': [''], 'paswd2': [''], 'plogin': ['']}>

        """
    if request.POST and 'vlogin' in request.POST:
        """
        <QueryDict: {'csrfmiddlewaretoken': ['RPrybHsYSgbQh8rqUMXzh0SzHQgVZQlN9XeXabocSwjH9peSEPVvM4Daf6np0kfi'], 
        'name': [''], 'email': [''], 'address': [''], 'phonenumber': [''], 'stndname': [''], 'vnumber': [''],
        'pass1': [''], 'pass2': [''], 'vlogin': ['']}>

        """
       
        
    return render(request,'register_login.html')

