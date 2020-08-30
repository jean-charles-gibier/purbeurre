import pprint

from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from user.forms import CustomUserCreationForm
# from django.contrib.auth.models import User


def dashboard_section(request, section='default'):
    print("DASHBOARD :: section : {}".format(section))
    return render(request, "user/dashboard.html")


def dashboard(request):
    pprint.pprint(request)
    return render(request, "user/dashboard.html")


def user(request):
    """ Exemple de page non valide """
    return HttpResponse("""
        <h1>Bienvenue sur la page des users !</h1>
        <p></p>
    """)
            

def register(request):

    if request.method == "GET":
        print("REGISTER GET :: {}".format("OK"))
        initial_values = {}
        if request.user is not None and not request.user.is_anonymous:
            initial_values['username'] = request.user.username
            initial_values['email'] = request.user.email
        return render(
            request, "user/register.html",
            {"form": CustomUserCreationForm(initial=initial_values)}
        )

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        form.fields['username'].widget.render_value = True
        pprint.pprint(form)
        print("REGISTER :: {}".format("OK"))
        pprint.pprint(request.POST)

        if form.is_valid():
            user = form.save()
        else:
            messages.add_message(request, messages.ERROR, "Les données sont invalides. Veuillez saisir à nouveau les identifiants.")
            print( "Les données sont invalides. Veuillez saisir à nouveau les identifiants.")
            return redirect(reverse('register'))

        print("REGISTER form.save() :: {}".format("OK"))

        auth_login(request, user)
        print("REGISTER login(request, user) :: {}".format("OK"))

        url_reverse = reverse("dashboard")
        print("REGISTER reverse('dashboard) :: {}".format("OK"))

        return redirect(url_reverse)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                #messages.add_message(request, messages.SUCCESS, "Vous êtes connecté.")
            else:
                messages.add_message(request, messages.ERROR, "Compte désactivé.")
        else:
            messages.add_message(
                request, messages.ERROR, "L'email et/ou le mot de passe sont invalides. Veuillez saisir à nouveau vos identifiants ou créer un compte.")
            return redirect(reverse('login'))
        return redirect(reverse('dashboard'))
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

