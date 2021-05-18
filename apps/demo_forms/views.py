from django.shortcuts import render, redirect

from .forms.user import UserForm
from .forms.hobbie import HobbieForm
from .forms.customForms import LoginForm

def index(request):
    return redirect("/") 


def register(request):
    if request.method == 'GET':
        form = UserForm()  
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['logged_user'] = user.name
            return redirect("/")  
    return render(request, 'register.html', {'form': form})      


def login(request):
    if request.method == 'GET':
        loginForm = LoginForm()
        return render(request, 'login.html', {'loginForm': loginForm})
    else:
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user = loginForm.login(request.POST)
            if user:
                request.session['logged_user'] = user.name
                return redirect("/")
        return render(request, 'login.html', {'loginForm': loginForm}) 

def logout(request):
    try:
        del request.session['logged_user']
    except:
        print('Error')
    return redirect('/')    


def hobbie(request):
    if request.method == 'GET':
        hobbieForm = HobbieForm()
    else:
        hobbieForm = HobbieForm(request.POST)
        if hobbieForm.is_valid():
            hobbieForm.save()
            return redirect("/")
    return render(request, 'hobbie.html', {'form': hobbieForm})    
     
