from django.shortcuts import render

# Create your views here.
def home(request):
	context_dict={'text':'hello','number':100}
	return render(request,'temp_app/home.html',context_dict)

def other(request):
	return render(request,'temp_app/other.html')

def reletive(request):
	return render(request,'temp_app/reletive_url.html')
