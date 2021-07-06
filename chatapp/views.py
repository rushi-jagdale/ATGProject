from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from chatapp.models import Message
from chatapp.forms import UpdateForm
from django.contrib import messages 
from chatapp.serializers import MessageSerializer, UserSerializer
import random






@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def register_view(request):
    """
    Render registration template
    """
    if request.method == 'POST':
        print("working1")
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
        return render(request, 'reg.html', {'form': form})
     
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 return redirect('chats')
    # else:
    #     print("working2")
    #     form = SignUpForm()
    # template = 'register.html'
    # context = {'form':form}
    # return render(request, template, context)
def home(request):
    name = request.user
    data = User.objects.filter(username=name)
    return render(request,'home.html',{'data':data})    

def login(request):
    
    if request.method == 'POST':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        username = request.POST['username']
        password = request.POST['password']
       
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)   
            return redirect('home')

        else:
            messages.info(request, 'invalid username and password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        cap = request.POST['cap']
        captha = request.POST['captha']
        print(cap)
        print(cap)
       
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'username already taken..')
               
                return redirect('register')

           


            else: 
                if cap == captha:
                    user = User.objects.create_user(username=username,password=password1)
                    user.save()
                    messages.info(request, 'User Created Successfully ..')
                    print('user created')
                    return redirect('register')
                else:
                    messages.info(request, 'invalid captcha')
                    return redirect('register')


        else:
            messages.info(request, 'Password is not matching ..')
            print('password not matching')
            return redirect('register')
    
    else:
        num1 = random.randrange(10,99)
        num2 = random.randrange(10,99)
        num =num1 + num2
        fn = str(num1)
        sn = str(num2)
        return render(request,'register.html',{"fn":fn,"sn":sn,"num":num})



def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, 'chat.html',
                      {'users': User.objects.exclude(username=request.user.username)})


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "GET":
        return render(request, "messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Message.objects.filter(sender_id=receiver, receiver_id=sender)})

def search(request):
    query = request.GET['search']
    allposts = User.objects.filter(username=query)
    return render(request,'search.html',{'data':allposts})

    

def edit(request,id):
    data = User.objects.get(id = id)
    return render(request,'edit.html',{'data':data})

def update(request, id):

    data = User.objects.get(id=id)
    form = UpdateForm(request.POST,instance=data)
    if form.is_valid():

        form.save()  
        return redirect("home")  
    return render(request,'edit.html',{'data':data})   
        
#         data = User.objects.get(id=id)
#         username = request.POST['username']
#         user = User.objects.create_user(username=username,password=password1)
#         data = Doctor.objects.get(id=id)
#         #print(data)
#         form = DoctorForm(request.POST, instance = data)
#         p = form.is_valid()
#         #print('in this update',p)
        


def logout(request):
    auth.logout(request)
    return redirect('login')   

