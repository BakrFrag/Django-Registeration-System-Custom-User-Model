from django.shortcuts import render,redirect;
from myapp.forms import UserCreationForm,UserLoginForm;
from django.contrib.auth import get_user_model,login,logout;
from django import forms;
from django.db.models import Q;
MyUser=get_user_model();
def home(request):
    return render(request,"home.html");
def register(request):
        form=UserCreationForm();
        if request.method=="POST":
            form=UserCreationForm(request.POST);

            if form.is_valid():
                 form.save()
                 print("No You Are Registered");
                 return redirect('login');
        else:
            form=UserCreationForm();
        return render(request,"register.html",{'form':form});
def userlogin(request):
    #form=UserLoginForm();
    if request.method=="POST":
        form=UserLoginForm(request.POST);
        print(form.is_valid())
        if form.is_valid():
            value=form.cleaned_data.get('query');
            user=MyUser.objects.filter(Q(username__iexact=value)|Q(email__iexact=value)).distinct().first();
            login(request,user);
            return redirect("home");
    else:
        form=UserLoginForm();
    return render(request,"login.html",{'form':form})
def userlogout(request):
    logout(request);
    return redirect("home");
