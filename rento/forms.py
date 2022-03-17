from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from rento.models import Tenant, Rent, User

class TenantSignUpForm(UserCreationForm):
    """ interests = forms.ModelMultipleChoiceField(
        queryset=Rent.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    ) """

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_tenant = True
        user.save()
        tenant = Tenant.objects.create(user=user)
        #tenant.interests.add(*self.cleaned_data.get('rents'))
        return user


class LandlordSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_landlord = True
        if commit:
            user.save()
        return user

class TenantPayRentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ('name','house_no','amount_paid' )
        """ widgets = {
            'interests': forms.CheckboxSelectMultiple
        } """
