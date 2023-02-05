from decouple import config
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .forms import RegisterUserForm
from .tokens import account_activation_token

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, (f'{username} welcome to IAS management system!'))
            return redirect('home')
        else:
            messages.success(request, ('''
            Sorry your username or password does not match!.
            Please enter a valid username or password and try again
            Thank you'''))
            return redirect('granted',)
    else:

        return render(request, 'login.html', {})


# Logout user
def logout_user(request):
    messages.success(request, ('Logout successful!'))
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        from_email = config('EMAIL_HOST_USER')
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            receiver = [to_email]
            send_mail(mail_subject, message, from_email,
                      receiver, fail_silently=False)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    model = User
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = model.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
