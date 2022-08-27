from django.shortcuts import render
from .models import *

def Index(request):
	md = MetaDatos.objects.all().last()
	title = md.title
	logo = md.logo
	number_phone = md.number
	title_banner = md.title_banner
	return render(request,'brujos.html',{'title':title,'logo':logo,'number':number_phone,'title_banner':title_banner})
