# from django.shortcuts import render, redirect
# from .forms import PersonForm
# from django.contrib.auth import login as auth_login
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate
# from .models import persona

# def register(request):
#     form = PersonForm()
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('home')

#     context = {'form': form}
#     return render(request, 'register.html', context)


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect('register')
#         else:
#             messages.info(request, 'Username or Password incorrect')
#             return render(request, 'login.html')
#     return render(request, 'login.html')
