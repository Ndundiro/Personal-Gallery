from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    print(images)
    return render(request, 'index.html', {'images':images[::-1], 'locations':locations})






def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_Category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



def image(request, image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'image.html', {"image":image})
