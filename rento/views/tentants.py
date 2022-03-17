from email import message
from pyexpat import model
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

#function-based views imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from ..decorators import tenant_required,landlord_required

#class based views imports
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



from ..models import Rent,RentDetails

from ..forms import TenantSignUpForm,TenantPayRentForm
from ..models import User

class TenantSignUpView(CreateView):
    model = User
    form_class = TenantSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tenant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tenants:pay_rent')

@login_required
@tenant_required
def show_rent_paid(request,pk):
    rent_paid = get_object_or_404(RentDetails, pk=pk)
    tenant = request.user.tenant

    return render(request,'rento/tenants/show_rents.html',{'rent_paid':rent_paid})

@method_decorator([login_required,tenant_required], name='dispatch')
class TenantPayRent(CreateView):
    model = Rent
    form_class = TenantPayRentForm
    template_name = 'rento/tenant/pay_rent_form.html'
    #success_url = reverse_lazy('tenants:tenant_list')
    success_url = reverse_lazy('/')

    def get_object(self):
        return self.request.user.tenant
    def form_valid(self, form):
        message.success(self.request,'Rent paid with success!')
        return super().form_valid(form)

        