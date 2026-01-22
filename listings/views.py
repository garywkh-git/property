from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import district_choices, rooms_choices, listing_type_choices, status_choices, price_choices, area_choices, property_age_choices   
from django.db.models import Q
from decimal import Decimal
# Create your views here.
def listings(request):
    listings = Listing.objects.filter(is_published=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context  = {"listings" : paged_listings}
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing" : listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(description__icontains=keywords) | Q(title__icontains=keywords)|Q(salesperson__name__icontains=keywords))
     # District       
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
    # Rooms
    rooms_range = request.GET.get('rooms_range')
    if rooms_range:
        try:
            min_rooms_str, max_rooms_str = rooms_range.split('-')
            min_rooms = int(min_rooms_str.strip())
            max_rooms = int(max_rooms_str.strip())
            queryset_list = queryset_list.filter(
                rooms__gte=min_rooms,
                rooms__lte=max_rooms
        )
        except (ValueError, TypeError):
            pass

    # Status (sale/rent)
    if 'status' in request.GET:
         status = request.GET['status']
         if status:
             queryset_list= queryset_list.filter(status__iexact=status)

    price_range = request.GET.get('price_range')
    if price_range:
        try:
            min_price_str, max_price_str = price_range.split('-')

            # Convert to float and scale to millions
            min_price = float(min_price_str) * 1_000_000
            max_price = float(max_price_str) * 1_000_000

            queryset_list = queryset_list.filter(
            price__gte=min_price,
            price__lte=max_price
        )
        except (ValueError, TypeError):
            pass  # ignore if format is wrong

    # Area (sqft)
    area_range = request.GET.get('area_range')
    if area_range:
            try:
                if area_range.endswith('+'):  # handle "2000+ sqft"
                    min_area = Decimal(area_range.replace('+', '').strip())
                    queryset_list = queryset_list.filter(area__gte=min_area)
                else:
                    min_area_str, max_area_str = area_range.split('-')
                    min_area = Decimal(min_area_str.strip())
                    max_area = Decimal(max_area_str.strip())
                    queryset_list = queryset_list.filter(
                        area__gte=min_area,
                        area__lte=max_area
            )
            except (ValueError, TypeError):
                pass

    # Property Age
    property_age_range = request.GET.get('property_age_range')
    if property_age_range:
        try:
            if property_age_range.endswith('+'):  # e.g. "20+"
                min_age = int(property_age_range.replace('+', '').strip())
                queryset_list = queryset_list.filter(age__gte=min_age)   #  use age
            else:
                min_age_str, max_age_str = property_age_range.split('-')
                min_age = int(min_age_str.strip())
                max_age = int(max_age_str.strip())
                queryset_list = queryset_list.filter(
                    age__gte=min_age,   #  use age
                    age__lte=max_age
            )
        except (ValueError, TypeError):
            pass


    paginator = Paginator(queryset_list,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "listings" : paged_listings,
        'district_choices': district_choices,
        'rooms_choices': rooms_choices,
        'status_choices': status_choices,
        'listing_type_choices': listing_type_choices,
        'price_choices': price_choices,
        'area_choices': area_choices,
        'property_age_choices': property_age_choices,
        'values' : request.GET,
        # 'price': request.GET.get('price'),
        # 'area': request.GET.get('area'),
        # 'property_age': request.GET.get('property_age'),


    }
    return render(request, 'listings/search.html', context)
