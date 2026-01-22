from django.shortcuts import render
from listings.models import Listing
from salespersons.models import Salesperson
from listings.choices import district_choices, listing_type_choices, status_choices, rooms_choices, price_choices, area_choices, property_age_choices
#from django.http import HttpResponse
# Create your views here.

# 
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {"listings": listings,
               "district_choices" : district_choices,
               "listing_type_choices" : listing_type_choices,
               "status_choices" : status_choices,
               "rooms_choices" : rooms_choices,
               "price_choices" : price_choices,
               "area_choices" : area_choices,
               "property_age_choices" : property_age_choices,
               }
    return render(request,'pages/index.html', context)
    
    
def about(request):
    salespersons = Salesperson.objects.order_by("-hire_date")[:3]
    mvp_salespersons = Salesperson.objects.all().filter(is_mvp=True)
    context = {"salespersons" : salespersons, "mvp_salespersons" : mvp_salespersons}
    #print(request,request.path)
    return render(request,'pages/about.html', context)