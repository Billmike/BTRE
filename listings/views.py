from django.shortcuts import render
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

from .models import Listing

# Create your views here.
def listings(request):
  all_listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(all_listings, 6)

  page = request.GET.get('page')

  paged_listing = paginator.get_page(page)

  context = {
    'all_listings': paged_listing
  }
  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  return render(request, 'listings/listing.html')

def search(request):
  return render(request, 'listing/search.html')