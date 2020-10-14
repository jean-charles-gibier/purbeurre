
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from user.forms import CustomUserCreationForm, CustomUserChangeForm

import pprint

def dashboard_section(request, section='default'):
    print("DASHBOARD :: section : {}".format(section))
    return render(request, "user/dashboard.html")


def dashboard(request):
    return render(request, "user/dashboard.html")


def user(request):
    """ Exemple de page non valide """
    return HttpResponse("""
        <h1>Bienvenue sur la page des users !</h1>
        <p></p>
    """)


def register(request):

    # Are we in modification mode or in creation ?
    is_modification = request.path.endswith('modify/') 
    CustomizedForm = CustomUserChangeForm if is_modification else CustomUserCreationForm

    if request.method == "GET":
        initial_values = {}
        if request.user is not None and not request.user.is_anonymous:
            initial_values['first_name'] =request.user.first_name
            initial_values['last_name'] =request.user.last_name
            initial_values['username'] = request.user.username
            initial_values['email'] = request.user.email
 
        return render(
            request, "user/register.html",
            {"form": CustomizedForm(initial=initial_values)}
        )

    elif request.method == "POST":
        if not is_modification:
            form = CustomizedForm(request.POST)
            form.fields['username'].widget.render_value = True
        else:
            form = CustomizedForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
        else:
            messages.add_message(request, messages.ERROR,
                                 "Les données sont invalides."
                                 " Veuillez saisir à nouveau les "
                                 "identifiants.")
            return render(request, 'user/register.html', {'form': form})

        auth_login(request, user)
        url_reverse = reverse("dashboard")
        return redirect(url_reverse)


def login(request):
    """
    :param request:
    :return: render ok => dashboard  ko =>  login
    """

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
            else:
                messages.add_message(request,
                                     messages.ERROR,
                                     "Compte désactivé.")
        else:
            messages.add_message(
                request, messages.ERROR, "L'email et/ou le mot de passe "
                                         "sont invalides. Veuillez saisir à"
                                         " nouveau vos identifiants ou "
                                         "créer un compte.")
            return render(request, 'registration/login.html', {'form': form})
        return redirect(reverse('dashboard'))
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
