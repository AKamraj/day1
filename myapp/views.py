from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from myapp import support_functions
from myapp.models import Currency


# Create your views here.
# every function in the views.py has a request parameter
def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    data['time_of_day'] = time
    return render(request, 'home.html', context=data)


def maintenance(request):
    data = dict()
    try:
        choice = request.GET['selection']
        if choice == "currencies":
            support_functions.add_currencies(support_functions.get_currency_list())
        c_list = Currency.objects.all()
        #   print("Got c_list", len(c_list))
        data['currencies'] = c_list
    # return HttpResponseRedirect(reverse('currencies'))
    except:
        pass  # pyton placeholder for do nothing
    return render(request, "maintenance.html", context=data)


def view_currencies(request):
    data = dict()
    c_list = Currency.objects.all()
    data['currencies'] = c_list
    return render(request, 'currencies.html', context=data)
