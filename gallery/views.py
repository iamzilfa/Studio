from django.shortcuts import render
from .models import Image, Location

def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    
    return render(request, 'all-photos/index.html',{'images': images[::-1], 'locations': locations}) 

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)

    return render(request, 'all-photos/location.html', {'location_images': images})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")  
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        
        return render(request, 'all-photos/search.html', {"message": message, "images": searched_images}) 
    else:
        message = "Search for any Image Category"

        return render(request, 'all-photos/search.html', {"message": message})