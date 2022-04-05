from django.shortcuts import render,HttpResponse,redirect
from .models import Petdb,Detaildb
from .forms import signupform,detailform
from django.contrib.auth import logout
from Petgrooming import settings
from django.core.mail import send_mail
import random
import requests
import json


# Create your views here.

def home(request):
    if request.method=='POST':
        if request.POST.get('Signup')=='Signup':
            Signupfrm=signupform(request.POST)
            if Signupfrm.is_valid():
                Signupfrm.save()
                print('Signup Successfully')
                otp=random.randint(1111,9999)
                #send mail
                sub="Success"
                msg=f"Hello user, \n Your account has been created successfully,\n Your OTP is{otp}"
                email_from = settings.EMAIL_HOST_USER
                to_email=['krutidhoja@gmail.com', 'patelvishva2001@gmail.com']
                send_mail(sub,msg,email_from,to_email)

                #send Message
                # mention url
                url = "https://www.fast2sms.com/dev/bulk"


                # create a dictionary
                my_data = {
                    # Your default Sender ID
                    'sender_id': 'FSTSMS',
                    
                    # Put your message here!
                    'message': f'Your OTP is {otp}',
                    
                    'language': 'english',
                    'route': 'p',
                    
                    # You can send sms to multiple numbers
                    # separated by comma.
                    'numbers': '9428230907,6356633872,7016210249'	
                }

                # create a dictionary
                headers = {
                    'authorization': 'q3wERzjd4vaOfAbUiXh5FpyrLmnKx0Poc8e9ksVIuDYJWtgBlT1ITujLVwJm0qYWaChOEnfoAgH8SxRF',
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache"
                }

                # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
                #load json data from source
                returned_msg = json.loads(response.text)

                # print the send message
                print(returned_msg['message'])
                return redirect('/')
            else:
                print(signupfrm.errors)
        elif request.POST.get('Login')=='Login':
            unm=request.POST['email']
            pas=request.POST['password']

            userid=Petdb.objects.get(password=pas)
            print("Userid:", userid.id)
            signup=Petdb.objects.filter(email=unm, password=pas)
            if signup:
                    print("Login successfully")
                    request.session['signup']=unm
                    request.session['userid']=userid.id
                    return redirect('required_details')
            else:
                print("login failed....try again")
        else:
            print('somthing went wrong')                     
    return render(request, 'home.html')


def profile(request):
    user=request.session.get('signup')
    userid=request.session.get('userid')
    id=Petdb.objects.get(id=userid)
    if request.method=='POST':
        Signupfrm=signupform(request.POST)
        if Signupfrm.is_valid():
            Signupfrm=signupform(request.POST, instance=id)
            Signupfrm.save()
            print("Your profile data has been updated")
            return redirect('required_details')
        else:
            print(Signupfrm.errors)
    else:
        print("Error...Something went wrong!!")
    return render(request,'profile.html',{'user': user, 'userid':Petdb.objects.get(id=userid)})

def services(request):
    user=request.session.get('signup')
    return render(request, 'services.html', {'user': user})

def required_details(request):
    user=request.session.get('signup')
    if request.method=='POST':
        detailfrm=detailform(request.POST, request.FILES)
        if detailfrm.is_valid():
            detailfrm.save()
            print("File Uploaded Successfully")
            return redirect('required_details')
        else:
            print(detailfrm.errors)
    else:
        detailfrm=detailform()
    return render(request, 'required_details.html', {'user': user})

def contact(request): 
    user=request.session.get('signup')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    return render(request, 'contact.html', {'user': user})

def about(request):
    user=request.session.get('signup')
    return render(request, 'about.html', {'user': user})

def userlogout(request):
    logout(request)
    return render(request, 'home.html')


    