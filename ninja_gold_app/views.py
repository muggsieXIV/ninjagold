from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    if 'goldsum' not in request.session:

        request.session['goldsum'] = 0
    elif 'activity_log' not in request.session:
        request.session['activity_log'] = []

    return render(request, 'index.html')




def process(request):
    print(request.POST)
    if request.POST['location'] == "farm":
        rand_num = random.randint(10, 20)
        request.session['goldsum'] += rand_num
        request.session['activity_log'].append(f"Got {rand_num} of gold from {request.POST['location']}")

    elif request.POST['location'] == "cave":
        rand_num = random.randint(5, 10)
        request.session['goldsum'] += rand_num
        request.session['activity_log'].append(f"Got {rand_num} of gold from {request.POST['location']}")

    elif request.POST['location'] == "house":
        rand_num = random.randint(2, 5)
        request.session['goldsum'] += rand_num
        request.session['activity_log'].append(f"Got {rand_num} of gold from {request.POST['location']}")

    elif request.POST['location'] == "casino":
        rand_num = random.randint(-50, 50)
        request.session['goldsum'] += rand_num
        request.session['activity_log'].append(f"Got {rand_num} of gold from {request.POST['location']}")

    return redirect('/')

