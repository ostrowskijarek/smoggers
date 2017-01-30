from django.http import JsonResponse
from .models import GeoPoint
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

def get_points(request):
    objs = GeoPoint.objects.all()
    data = {}
    data["points"]=[]
    for obj in objs:
        point={"coordinates" : {"latitude" : str(obj.latitude), "longitude" : str(obj.longitude)}, "id" : obj.pk}
        data["points"].append(point)
    return JsonResponse(data)

def set_point(request):
    longitude =request.POST["lng"]
    latitude = request.POST["lat"]
    gp = GeoPoint(description="dummy description", timestamp=timezone.now(), latitude = latitude, longitude=longitude, author="dummy author" )
    gp.save()
    data={"id":gp.id}
    return JsonResponse(data)