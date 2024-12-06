from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserUpdateForm, CustomUserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#landing page
def landing_page(request):
    return render(request, 'user_authentication/app_landing.html')
# User registration view
def about_page(request):
    return render(request, 'user_authentication/about.html')
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Signed Up')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong, please try again')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_authentication/signup.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home_view')
        else:
            messages.error(request, 'Invalid Username or Password')
    return render(request, 'user_authentication/login.html')

# View for displaying and creating the user profile
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(request, 'user_authentication/profile.html', {'form': form, 'user': request.user})

# View for updating the user profile
@login_required
def profile_update_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(request, 'user_authentication/profile_update.html', {'form': form})

# Home view (requires login)
@login_required
def home_view(request):
    return render(request, 'user_authentication/home_view.html')

# User logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')
