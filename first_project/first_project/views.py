from django.http import HttpResponse

def home(request):
    print("Hello")
    return HttpResponse("<h1>Hello I am learning Django</h1>")