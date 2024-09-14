from django.shortcuts import render

# Create your views here.



def login(request):
    return render(request, 'store/login.html')




def register(request):
    return render(request, 'store/register.html')




def contact(request):
    return render(request, 'store/contact-us.html')