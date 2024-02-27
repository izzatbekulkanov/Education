from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('login-email')
        password = request.POST.get('login-password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print(request.POST)
            # Foydalanuvchi muvaffaqiyatli kiritildi, o'zgardi yoki kiritish qilishga o'tkazish
            return redirect('index')  # O'zgardi yoki kiritishdan so'ng o'tkaziladigan URL
        else:
            # Foydalanuvchi kiritishi yoki parol xato
            return render(request, 'register/login.html', {'error_message': 'Invalid email or password'})
    else:
        return render(request, 'register/login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')  # Kiritilgan parolni olish
            form.instance.set_password(password)  # Parolni hashlash
            form.instance.password_save = password  # password_save ga matn korinishida saqlash
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/register.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')  # Foydalanuvchi avtorizatsiyadan chiqqandan so'ng o'tkaziladigan URL

def user_list_view(request):
    return render(request, 'app/users/users_list.html')

