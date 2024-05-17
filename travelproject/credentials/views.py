from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request): #assigning the values from register.html to variables
    if request.method == 'POST':
        u_name = request.POST['username']
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        mail = request.POST['email']
        p_word = request.POST['password']
        cp_word = request.POST['password1']

        if p_word == cp_word:
            if User.objects.filter(username=u_name).exists():#checking if the username exists in the database.
                messages.info(request,'username taken')
                return redirect('register')

            elif User.objects.filter(email=mail).exists():#checking if the mail id exists in the database.
                messages.info(request,'email taken')
                return redirect('register')

            else: #adding the data to the fields in the database.
                user = User.objects.create_user(username=u_name, password=p_word, first_name=f_name, last_name=l_name, email=mail )
                user.save();# saving the user.
                return redirect('login')

        else:
            messages.info(request,'password mismatch')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

