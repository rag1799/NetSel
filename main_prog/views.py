from django.shortcuts import render
import joblib
#import sklearn.external.joblib as extjoblib
#import joblib
import numpy as np
import random as rnd
from datetime import datetime

# Create your views here.
def home(request):
    if request.method =="POST":
        model = joblib.load("load_model.pkl")
        scaler = joblib.load("scaler.pkl") 

        area = int(request.POST.get("local_area"))
        duration = int(request.POST.get("dur"))*60
        rate = int(request.POST.get("rating"))
        num1 = rnd.randint(6000000000, 9999999999)
        num2 = rnd.randint(6000000000, 9999999999)
        while num1 == num2:
            num2 = rnd.randint(6000000000, 9999999999)
        date_now = datetime.now()
        date_now = date_now.toordinal()

        x = []
        x.append(num1)
        x.append(num2)
        x.append(duration)
        x.append(rate)
        x.append(area) 
        x.append(date_now)
        y = [x]
    
        #x=[[6788901239,7655234567,4513,2,215.91,0,737170]]
        z = np.array(y)
        z = z.reshape(1,-1)
        sc = scaler.transform(z)
        predict = model.predict(sc)
        op = 'BSNL'
        if predict[0] == 0:
            op = 'Jio'
        elif predict[0] == 1:
            op ='Airtel'
        elif predict[0] == 2:
            op ='Vodafone'   
        return render(request,"new_page.html",{"op":op})    

        
    return render(request,"new_page.html")