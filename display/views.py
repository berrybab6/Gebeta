from django.shortcuts import render
from .models import Food,Chief
import random
# Create your views here.
def addchief(request):
    ch=Chief.objects.all()
    return render(request,'aboutus.html',{'chief':ch})

def addfood(request):
    foodP=Food.objects.all().filter(promot=True)
    lis_prom=list(foodP)
    
    ch=Chief.objects.all().order_by('points')
    lis=list(ch)

    
    #ch_Promot=Chief.objects.all().order_by('exprience')
    #lis_prom=list(ch_Promot)

    food=Food.objects.all().filter(isTraditional=True)
    food_trad=random.choice(food)


    
    return render(request,'index.html',{'food':food_trad,'chief':lis[-1],'foodProm':lis_prom[-1]})

def promotechief(request):
    
    return render(request,'index.html')

  
def myMax(list1): 
    max = list1[0]  
    for x in list1: 
        if x > max : 
            max = x 
    return max