from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth import views as auth_views


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.save()
            return render(request,
                          'account/signup/registration_done.html',
                          {'user': user})
    else:
        form = UserRegistrationForm()
    return render(request, 'account/signup/registration.html', {'form': form})


class UserLoginView(auth_views.LoginView):
    template_name = 'account/authentication/login.html'


class UserLogoutView(auth_views.LogoutView):
    template_name = 'account/authentication/logged_out.html'