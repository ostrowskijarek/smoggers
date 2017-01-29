# import it
from django.http import JsonResponse

def get_points(request):
    data =  {"points" : [{\
	"id" : 1, \
	"coordinates":{ \
	"latitude":"51.17145", \
	"longitude":"17.19718"}},	\
	{"id" : 2, \
	"coordinates":{ \
	"latitude":"51.1823", \
	"longitude":"17.1827"}},	\
	{"id" : 3, \
	"coordinates":{ \
	"latitude":"51.2213", \
	"longitude":"17.1227"}}]}	\

    return JsonResponse(data)
	
