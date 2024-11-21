from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def age_view(request):
    # username = request.GET.get('name','')
    username = request.GET['name']
    response = render(request,'testapp/age.html',{'name':username})
    response.set_cookie('name',username)
    return response

def gf_view(request):
    username = request.COOKIES['name']
    age = request.GET['age']
    response = render(request,'testapp/gf.html',{'name':username})
    response.set_cookie('age',age)
    return response

def index_view(request):
    username = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.GET['gf']
    response = render(request,'testapp/index.html',{'name':username,'age':age,'gf':gf})
    # response.set_cookie('gf',gf)
    return response