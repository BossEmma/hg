from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'index.html')
  
def facebook(request):
  return render(request, 'facebook.html')
  
def instagram(request):
  return render(request, 'instagram.html')
  
def tiktok(request):
  return render(request, 'tiktok.html')