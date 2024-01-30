from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.shortcuts import redirect


def activation(request, uid, token):
    try:
        # Decode the user ID and check if it's a valid user
        uid = force_str(urlsafe_base64_decode(uid))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    # Check if the user exists and the token is valid
    if user is not None and default_token_generator.check_token(user, token):
        # Activate the user account
        user.is_active = True
        user.save()
        print(user)

        # Optionally, you can log the user in automatically after activation
        # from django.contrib.auth import login
        # login(request, user)

        messages.success(request, 'Your account has been activated successfully. You can now log in.')
        return redirect('success')
    else:
        messages.error(request, 'Invalid activation link. Please try again.')
        return redirect('fail')


def login_view(request, uid, token):
    context = {'uid': uid, 'token': token}
    return render(request, 'login.html', context)


def success(request):
    return render(request, 'success.html')


def fail(request):
    return render(request, 'fail.html')
