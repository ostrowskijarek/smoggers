from django.http import JsonResponse
from geopy.distance import vincenty
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
def get_containers(request):
    pix_min = request.POST["pix_min"]
    pix_max = request.POST["pix_max"]
    cur_zoom = int(request.POST["cur_zoom"])
    print(request.POST)
    data = {}
    data["points"]=[]
   
    objs = GeoPoint.objects.all()
    radius = int(300 * (1+ ((14-cur_zoom)) * ((14-cur_zoom)) * ((14-cur_zoom))))
    print(radius)
    data["radius"]=radius
    centers=[]
    taken_list=[]
    centers.append(objs[0])
    for obj in objs:
        flagToAdd=True
        for c in centers:  
           
            if (vincenty((obj.latitude, obj.longitude),(c.latitude, c.longitude)).meters) < radius: 
                if obj.pk != c.pk:
                   flagToAdd=False
                   if not obj.pk in taken_list:
                       c.counter = c.counter+1
                       taken_list.append(obj.pk)
        if obj not in centers and flagToAdd:
           centers.append(obj)
    for c in centers:
        point={"coordinates" : {"latitude" : str(c.latitude), "longitude" : str(c.longitude)}, "id" : c.pk, "counter" : c.counter}
        data["points"].append(point)

    return JsonResponse(data)

def set_point(request):
    longitude =request.POST["lng"]
    latitude = request.POST["lat"]
    gp = GeoPoint(description="dummy description", timestamp=timezone.now(), latitude = latitude, longitude=longitude, author="dummy author" )
    gp.save()
    data={"id":gp.id}
    return JsonResponse(data)
