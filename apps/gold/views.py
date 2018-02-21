from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 0
	if not 'string' in request.session:
		request.session['string'] = " "
	if not 'loss' in request.session:
		request.session['loss'] = " "


	return render(request, "gold/index.html")


def process_money(request):
	if request.POST['building'] == 'farm':
		gain = random.randrange(10, 21)
		request.session['gold'] += gain
		request.session['string'] += "Earned "+str(gain)+" gold from the farm ("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")\n"
	if request.POST['building'] == 'cave':
		gain = random.randrange(5, 11)
		request.session['gold'] += gain
		request.session['string'] += "Earned "+str(gain)+" gold from the cave ("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")\n"
	if request.POST['building'] == 'house':
		gain = random.randrange(2, 6)
		request.session['gold'] += gain
		request.session['string'] += "Earned "+str(gain)+" gold from the house ("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")\n"
	if request.POST['building'] == 'casino':
		luck = random.randrange(-50, 51)
		request.session['gold'] += luck
		if luck >= 0:
			request.session['string'] += "Entered a casino and won "+str(luck)+" gold. Nice! ("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")\n"
		if luck < 0:
			luck += 50	
			request.session['loss'] += "Entered a casino and lost "+str(luck)+" gold. Shit... ("+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+")\n"

	request.session['loss_split'] = request.session['loss'].split('\n')
	print request.session['loss_split']
	request.session['split'] = request.session['string'].split('\n')
	print request.session['split']

	return redirect("/gold/")