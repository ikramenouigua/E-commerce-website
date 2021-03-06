from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserChangeForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from accounts.forms import CreateUserForm,SettingsForm

from .forms import CreateUserForm
from main.models import *
from .decorators import unauthenticated_user, allowed_users

#inscription d'un nouveau utilsateur 

@unauthenticated_user               #condition d'authentification
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        #tester la validite des champs
        if form.is_valid():
            user = form.save()
            userType = form.cleaned_data.get('choice')
           
            group = Group.objects.get(name=userType)
            user.groups.add(group)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

#connexion au compte en fournirant email et mot de passe
@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

#afficher les informations relatif a un compte 
@login_required
@allowed_users(allowed_roles=[ 'CLIENT','BOTH'])
def view_account(request):
    wishes = WishlistProduct.objects.filter(user=request.user)
    num_wishes = wishes.count()
    carts = Cart.objects.filter(user=request.user)
    num_carts = carts.count()
    total_price = 0
    for cart in carts:
        total_price += cart.cart_total_price()
    userform = User.objects.get(id=request.user.id)
    form = SettingsForm(instance=userform)
    
    if request.method == 'POST':

        form = SettingsForm(request.POST, instance=userform)
        print(form.name)
        if form.is_valid():
            form.save()
            return redirect('general')
    context = {'form': form,'products': wishes, 'num_wishes': num_wishes, 
               'num_carts': num_carts, 'total_price': total_price}
    return render(request, 'accounts/myAccount.html',context)


#modifier les informations d'un compte 
@login_required
@allowed_users(allowed_roles=[ 'CLIENT','BOTH'])
def edit_account(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account/profile/')
    return render(request, 'accounts/myAccount.html')


@login_required
@allowed_users(allowed_roles=[ 'CLIENT','BOTH'])
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password_reset/password_reset.html", context={"password_reset_form": password_reset_form})

#supprimer compte client
@login_required
@allowed_users(allowed_roles=[ 'CLIENT','BOTH'])
def delete_account_client(request):
    wishes = WishlistProduct.objects.filter(user=request.user)
    num_wishes = wishes.count()
    carts = Cart.objects.filter(user=request.user)
    num_carts = carts.count()
    total_price = 0
    for cart in carts:
        total_price += cart.cart_total_price()
    user=request.user
    if request.method == "POST":
        user.delete()
        return redirect('home')
    context = {'user': user,'products': wishes, 'num_wishes': num_wishes,
               'num_carts': num_carts, 'total_price': total_price}
    return render(request, 'accounts/delete_account.html', context)