from django.shortcuts import render


# Create your views here.
# every function in the views.py has a request parameter
def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    data['time_of_day'] = time
    return render(request, 'home.html', context=data)
