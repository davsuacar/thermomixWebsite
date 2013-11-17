
from django.http import HttpResponse
from django.shortcuts import render
from manuelaWebsite.forms import meetingRequestForm, contactForm
from django.http.response import HttpResponseRedirect
from manuelaWebsite.models import Recipe


def index(request):
    
    if request.method == 'POST': # If the form has been submitted...
        form = meetingRequestForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = meetingRequestForm() # An unbound form

    return render(request, 'home/index.html', {
        'form': form,
    })        

def recipes(request):
    
    recipes = Recipe.objects.all()
    
    return render(request, 'recipes/recipes.html', {'recipes': recipes})

def shop(request):
    return render(request, 'shop/shop.html', {})

def offers(request):
    return render(request, 'offers/offers.html', {})


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = contactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # SEND EMAIL
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = contactForm() # An unbound form

    return render(request, 'contact/contact.html', {
        'form': form,
    })