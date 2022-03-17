from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_tenant:
            return redirect('tenants:tenant_list')
        else:
            return redirect('landlord:landlord_list')
    return render(request, 'rento/home.html')