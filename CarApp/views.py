from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import SignupForm
from datetime import datetime
from .models import UserCar
from django.shortcuts import render, get_object_or_404
from .models import Ad
from .models import Contact
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.core.paginator import Paginator, Page
import joblib
import numpy as np
import os
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
BASE_DIR = settings.BASE_DIR


# Specify the absolute path to the scaler and model files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scaler_filename = r'D:\CarKoto\CarSell\model_files\min_max_scaler.save' 
model_path = r'D:\CarKoto\CarSell\model_files\xg_boost_model.pkl'

# Load the scaler and model using the variables you defined
scaler = joblib.load(scaler_filename)
model = joblib.load(model_path)




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            # You can add additional actions like sending a confirmation email
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# Create your views here.
def landingpage(request):

  
    return render(request, 'landingpage.html')
    #return HttpResponse("This is Homepage")

def home(request):
    
    return render(request, 'home.html')

def home2(request):
    
    return render(request, 'home2.html')    



def Carbuy(request):
    location_search = request.GET.get('location_search')

    if location_search:
        ads = Ad.objects.filter(location__iexact=location_search)
    else:
        ads = Ad.objects.all()

        

    paginator = Paginator(ads, 10)  # Show 10 ads per page
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page
    }    

    return render(request, 'CarBuy.html', {'ads': ads})

def CarSell(request):

    if request.method == "POST":

     # Retrieve the user
     user = request.user  # This will give you the currently logged-in user   
     cname = request.POST.get('cname') 
     phone = request.POST.get('phone') 
     location = request.POST.get('location')
     caddress = request.POST.get('caddress') 
     title = request.POST.get('title')
     brand = request.POST.get('brand')
     mileage = request.POST.get('mileage')
     model = request.POST.get('model')
     registration = request.POST.get('registration')
     price = request.POST.get('price')
     description = request.POST.get('description')
     image1 = request.FILES.get('image1')
     image2 = request.FILES.get('image2')
     image3 = request.FILES.get('image3')
     image4 = request.FILES.get('image4')
     image5 = request.FILES.get('image5')
   

     CarSell = Ad(user=user,cname=cname,phone=phone,location=location,caddress=caddress,mileage=mileage,title=title,brand=brand,model=model,registration=registration,price=price,description=description,image1=image1,image2=image2,image3=image3,image4=image4,image5=image5) 
     
     CarSell.save()

     messages.success(request, "Your Ad has been posted in CarAds!")

    return render(request, 'CarSell.html', {'LOCATION_CHOICES': Ad.LOCATION_CHOICES})
   

    return render(request,'CarSell.html')         

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent! ")

    return render(request,'contact.html')  
    

def CPP(request):

    return render(request,'CPP.html')  

def about(request):

    return render(request,'about.html') 

def about2(request):

    return render(request,'about2.html')     

def Egarage(request):

    if request.method == "POST":
        car_name = request.POST.get('car_name')
        car_model = request.POST.get('car_model')
        client_name = request.POST.get('client_name')
        client_mobile = request.POST.get('client_mobile')
        client_address = request.POST.get('client_address')
        car_problem = request.POST.get('car_problem')
        booking_date = request.POST.get('booking_date')
        Egarage = UserCar(car_name=car_name,car_model=car_model,client_name=client_name,client_mobile=client_mobile,client_address=client_address,car_problem=car_problem, booking_date=booking_date)
        Egarage.save()
        messages.success(request, "Your Appointment has been taken! ")
        


    return render(request,'Egarage.html')  

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Specify your login template here
    

    def get_success_url(self):
        # Customize the success URL based on your requirements
        return reverse_lazy('home2')  # Redirect to 'home' page 
        messages.success(self.request, "You are successfully logged in.")

class CustomLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('landingpage')  # Adjust the URL name as needed                    




def car_detail(request, car_id):
    ad = get_object_or_404(Ad, id=car_id)
    return render(request, 'car_detail.html', {'ad': ad}) 
    


def cpp_view(request):

    return render(request, 'CPP.html')

def get_price(transmission ,fuel_type,  brand, car_model, registration, model_year, body_type, engine_capacity, kilometers_run):
    brand_dict = {'Chevrolet': 0, 'Ford': 1, 'Ford': 2, 'Honda': 3, 'Hyundai': 4, 'Kia': 5, 'Mahindra': 6, 'Maruti Suzuki': 7, 'Mazda': 8, 'Mitsubishi': 9, 'Nissan': 10, 'Proton': 11, 'SsangYong': 12, 'Suzuki': 13, 'Tata': 14, 'Toyota': 15, 'BMW':16}
    body_type_dict = {'Estate': 0, 'Hatchback': 1, 'MPV': 2, 'SUV / 4x4': 3, 'Saloon': 4}
    car_model_dict = {'320i': 0, '5 Series': 1, 'APV': 2, 'Accent': 3, 'Allion': 4, 'Alphard': 5, 'Alto': 6, 'Alto 800': 7, 'Aqua': 8, 'Attrage': 9, 'Auris': 10, 'Avanza': 11, 'Axela': 12, 'Axio': 13, 'Bluebird': 14, 'C-Class': 15, 'C-HR': 16, 'CR-V': 17, 'CR-Z': 18, 'CX-7': 19, 'Cami': 20, 'Camry': 21, 'Carina': 22, 'Carryboy': 23, 'Cefiro': 24, 'City': 25, 'CityRover': 26, 'Civic': 27, 'Coaster': 28, 'Corolla': 29, 'Corona': 30, 'Corsa': 31, 'Crown': 32, 'Discovery': 33, 'Dualis': 34, 'Dyna': 35, 'E 250': 36, 'Eco Sport': 37, 'Esquire': 38, 'Estima': 39, 'Fielder': 40, 'Fiesta': 41, 'Fit': 42, 'GLA-Class': 43, 'GLX': 44, 'Grace': 45, 'H-RV': 46, 'H1': 47, 'H2': 48, 'HR-V': 49, 'Harrier': 50, 'Hiace': 51, 'Hilux': 52, 'Ikon': 53, 'Indigo Ecs': 54, 'Insight': 55, 'Juke': 56, 'Kluger': 57, 'Kyron': 58, 'Lancer': 59, 'Land Cruiser': 60, 'LiteAce': 61, 'MPV': 62, 'MR2': 63, 'Mark II': 64, 'Murano': 65, 'NX': 66, 'Noah': 67, 'Note': 68, 'Other Model': 69, 'Outlandar': 70, 'Outlander': 71, 'Pajero': 72, 'Passo': 73, 'Pathfinder': 74, 'Prado': 75, 'Premio': 76, 'Prius': 77, 'Probox': 78, 'Q5': 79, 'RAV4': 80, 'RVR': 81, 'RX': 82, 'RX-8': 83, 'Ractis': 84, 'Raum': 85, 'RunX': 86, 'Rush': 87, 'S660': 88, 'Santa Fe': 89, 'Satria': 90, 'Sienta': 91, 'Sonata': 92, 'Spacio': 93, 'Spark': 94, 'Sportage': 95, 'Sprinter': 96, 'Starlet': 97, 'Starlet Soleil': 98, 'Succeed': 99, 'Sunny': 100, 'Swift': 101, 'Terrano': 102, 'Tiida': 103, 'TownAce': 104, 'Tucson': 105, 'Urvan': 106, 'V6': 107, 'Vezel': 108, 'Vista': 109, 'Vitz': 110, 'WagonR': 111, 'Wish': 112, 'X Assista': 113, 'X-Trail': 114, 'XJ': 115, 'Yaris': 116, 'ist': 117, 'l200': 118, 'l300': 119, 'Belta':120}
    features = ['Automatic', 'CNG and OIL', 'HYBRID', 'LPG and OIL', 'OIL', 'brand', 'car_model' ,'registration','model_year', 'body_type', 'engine_capacity', 'kilometers_run']
    scale_vars = ['Automatic', 'CNG and OIL', 'HYBRID', 'LPG and OIL', 'OIL','body_type','engine_capacity','kilometers_run']

    # deciding fuel type
    cng_and_oil = 0
    hybrid = 0
    lpg_and_oil = 0
    oil = 0
    if fuel_type == 'CNG and OIL':
        cng_and_oil = 1
    elif fuel_type == 'HYBRID':
        hybrid = 1
    elif fuel_type == 'LPG and OIL':
        lpg_and_oil = 1
    elif fuel_type == 'OIL':
        oil = 1


    # deciding transmission type
    if transmission == '1':
        automatic = 1
    else:
        automatic = 0


    test_array = [ automatic , cng_and_oil , hybrid, lpg_and_oil, oil, brand_dict[brand], car_model_dict[car_model], registration, model_year, body_type_dict[body_type], engine_capacity, kilometers_run]
    test_array = np.array(test_array) # convert into numpy array
    
    test_array = test_array.reshape(1,-1) #reshape
    test_df = pd.DataFrame(test_array, columns = features)
 
    # scaling data
    scaler = joblib.load(scaler_filename)
    scaler.clip = False
    test_df[scale_vars] = scaler.transform(test_df[scale_vars])

    # declare path where you saved your model
    model_path = r'D:\CarKoto\CarSell\model_files\xg_boost_model.pkl'
    # open file
    file = open(model_path, "rb")
    # load the trained model
    trained_model = joblib.load(file)

    prediction = int(trained_model.predict(test_df))
    return prediction 

def predict_price(request):
    if request.method == 'POST':
        transmission = request.POST.get('transmission')
        fuel_type = request.POST.get('fuel_type')
        brand = request.POST.get('brand')
        car_model = request.POST.get('car_model')
        registration = int(request.POST.get('registration'))
        model_year = int(request.POST.get('model_year'))
        body_type = request.POST.get('body_type')
        engine_capacity = int(request.POST.get('engine_capacity'))
        kilometers_run = int(request.POST.get('kilometers_run'))

        # Call the get_price function to make predictions
        prediction = get_price(transmission, fuel_type, brand, car_model, registration, model_year, body_type, engine_capacity, kilometers_run)

        # Prepare the response
        response_data = {'predicted_price': prediction}

        return render(request, 'CPP.html', response_data)

    return render(request, 'CPP.html')






