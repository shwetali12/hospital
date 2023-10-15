from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

def index(request):
    return render(request,'index.html')

def doctor(request):
    return render(request,'doctor.html')

def patient(request):
    return render(request,'patient.html')

def register(request):
    msg = None
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        form = SignupForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            if pass1!=pass2:
                return HttpResponse("Your Password1  and password2 are not same.")
            else:
                user = form.save()
                login(request, user)  # Log in the user
                return redirect('index')
            # After saving the user, you should log them in.
          # Redirect to the desired page after registration
        else:
            print('not valid')
            
    else:
        form = SignupForm()

    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
   
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_patient:
                login(request, user)
                return redirect('patient')
            elif user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor')

            else:
                print('Invalid credentials')
        else:
            print=('Error validating form')
        
    return render(request, 'login.html', {'form': form})
