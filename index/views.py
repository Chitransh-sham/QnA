from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth
from math import ceil
from .models import Registration
from .models import contactus 
from .models import postdata , Message
from django.http import HttpResponse, JsonResponse
# Create your views here.
def index(request):
    contex = {}
    
    check = Registration.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = Registration.objects.get(user__id=request.user.id)
        contex["data"]=data
    
    if request.user.is_authenticated:
        posts=postdata.objects.all()
        contex["posts"]=posts
        
    result=render(request,'index.html',contex)
    return result
    

#----------------------------------------Login-----------------------------------------#

#----------------------------------------Registration--------------------------------------#

#----------------------------------------Contact---------------------------------------#
def contact(request):
    result = render(request,'contact.html')
    return result
    
#----------------------------example----------------------------#
def example(request):
    result=render(request,'contactmess.html')
    return result
#-----------------------------------------Ragistration---------------------------------#
def ragister(request):
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        userID=request.POST['userID']
        email=request.POST['email']
        password=request.POST['password']
        cn=request.POST['contactNO']
        users1 = User.objects.create_user(first_name=first_name,last_name=last_name,username=userID,email=email,password=password)
        users1.save()
        a = Registration(user=users1,contactNO=cn)
        a.save()
        return redirect('login')
    else:
        return render(request,'register.html')

#---------------------------------------ContactUs---------------------------------------#
def feedback(request):
    if(request.method=='POST'):
        userID=request.POST['userid']
        email=request.POST['email']
        message=request.POST['message']
        users = contactus(UserID=userID,email=email,message=message)
        users.save()
        return redirect('example.html')
    else:
        return render(request,'index.html')

#---------------------------------------Authentication-----------------------------#
def login(request):
    if(request.method=='POST'):
        username=request.POST['userID']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user!= None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
#--------------------------------------------------------Logout-------------------------------------------#
def logout(request):
    auth.logout(request)
    return redirect('index')            

#--------------------------------------------------Dashboard----------------------------------------------#

def dashboard(request):
    contex = {}
    check = Registration.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = Registration.objects.get(user__id=request.user.id)
        contex["data"]=data
    result = render(request,'dashboard.html',contex)

    return result

#------------------------------------------------edit-profile---------------------------------------------#
def edit_profile(request):
    contex = {}
    check = Registration.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = Registration.objects.get(user__id=request.user.id)
        contex["data"]=data
    result = render(request,'edit-profile.html',contex)
    return result
#-----------------------------------------------Profile_Update-----------------------------------------------------#
def update(request):
    contex = {}
    check = Registration.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = Registration.objects.get(user__id=request.user.id)
        contex["data"]=data
    if(request.method=='POST'):
            
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        profession=request.POST['profession']
        contactNO=request.POST['contactNO']
        email=request.POST['email']
        dob=request.POST['dob']
            
        user = User.objects.get(id=request.user.id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        user.save()

        data.contactNO = contactNO
        data.profession = profession
        data.date = dob
        data.save()

    if "img" in request.FILES:
        image = request.FILES["img"]
        data.image = image
        data.save()
        contex["status"] = "Changes Saved Successfully"
    return render(request,'dashboard.html',contex)
#----------------------------------------Question-----------------------------------------#
def question(request,pk):
    contex = {}
    data=postdata.objects.filter(user__id=request.user.id)
    contex["data"] = data

    if request.user.is_authenticated:
        
        if(request.method=='POST'):
            
            ques=request.POST['post_data']
            user1 = get_object_or_404(User,id=request.user.id) 
            
        if "post_img" in request.FILES:
            image = request.FILES["post_img"]
            r= get_object_or_404(Registration,pk=pk)  
            data=postdata(question=ques,user=user1,pimg=image,reg=r)
             
            data.save()
            contex["status"] ="{} Added Successfully".format(data.question)

    

    

    return render(request,"question.html",contex)
    
   

    

#----------------------------------------chat-----------------------------------------#
def chat(request):
    return render(request, 'chat.html')



def checkview(request):
    room = request.POST['roomname']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

