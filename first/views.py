from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'index.html', {})


def about(request):
	return render(request, 'about.html', {})

def default(request):
	return render(request, 'default.html', {})