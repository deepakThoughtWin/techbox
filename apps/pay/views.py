from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe
from stripe.api_resources import source
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from apps.authentication.models import Profile


stripe.api_key = "sk_test_51ImfcKSC4t3SvztxvzEY37TgMIkxD34qRwflOgBHZ7v3AAPnKcDrXP8OnTfckmp0hiICwl16ZoCnzRsqq3j9JJ0x00gqQ3jj2y"
# Create your views here.
@login_required
def index(request):
	return render(request, 'pay/index.html')

@login_required
def charge(request):
	amount = 100000
	if request.method == 'POST':
		print('Data:', request.POST)
		customer=stripe.Customer.create(
			email=request.user.email,
			name=request.user.username,
			source=request.POST['stripeToken'],
			)

		charge=stripe.Charge.create(
			customer=customer,
			amount=100*1000,
			currency='inr',
			description="Upgrade to Premium")
		queryset=Profile.objects.filter(id=request.user.id).update(upgraded=True)
		queryset1=Profile.objects.filter(id=request.user.id).update(upgraded_on=timezone.now())
	return redirect(reverse('pay:success'))

@login_required
def successMsg(request):
	amount = 1000
	return render(request, 'pay/success.html', {'amount':amount})