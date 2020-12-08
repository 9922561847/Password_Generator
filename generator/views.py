from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'index.html')
def password(request):
    characters = list('qwertyuiopasdfghjkzxcvbnm')
    if request.GET.get("upperCase"):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get("specialCharacters"):
        characters.extend(list('@$%^&&*!~?'))
    if request.GET.get("Numbers"):
        characters.extend(list('1234567890'))
    length = int(request.GET.get("length",12))
    thepassword = ''
    for i in range(length):
         thepassword += random.choice(characters)

    return render(request,'pass.html',{'pass':thepassword})