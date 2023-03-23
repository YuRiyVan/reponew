from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Product, Category, Product_img
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect


def redirect_view(request):
    response = redirect('/redirect-main/')
    return response


def main1(request):
    return redirect('http://127.0.0.1:8000/main/')


def base(request):
    return render(request, 'shop/base.html')


def contact(request):
    return render(request, 'shop/contact.html')


def about(request):
    return render(request, 'shop/about.html')


def main(request):
    data = Category.objects.all()
    return render(request, 'shop/main.html', {'data': data})


def basket(request):
    return render(request, 'shop/basket.html')


def forgot_password(request):
    return render(request, 'shop/forgot_password.html')


def category(request, id_cat):
    data = Product.objects.filter(category=id_cat)
    cat_name = Category.objects.get(category=id_cat)
    return render(request, 'shop/category.html', {'data': data, "name": cat_name.name})


def product(request, id_prod):
    data = Product.objects.get(id=id_prod)
    imag = Product_img.objects.filter(id=1)
    return render(request, 'shop/product.html', {"data": data}, {"imag": imag})


def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(
            username=data["username"], password=data["password"])
        if user != None:
            return redirect('/main/')
        else:
            # return HttpResponse("<h1> ВЫ НЕ АВТОРИЗОВАНЫ  </h1>")
            #user = User.objects.create_user(username = data["username"] , email = data["email"] , password = data["password"])
            # user.save()
            return redirect('/authorizd/')
    return render(request, "shop/auth.html")


def authorizd(request):
    user = None
    info = [{"У ВАС НЕТ АККАУНТА, ПОЖАЛУЙСТА ЗАРЕГИСТРИРУЙТЕСЬ"}, {
        "Вы успешно зарегистрировались. Приветствуем Вас на нашем сайте."}]
    if request.method == "POST":
        data = request.POST
        user = User.objects.create_user(
            username=data["username"], email=data["email"], password=data["password"])
        user.save()
    if user != None:
        return render(request, "shop/authorizd.html", {'info': info[1]})
    else:
        return render(request, "shop/authorizd.html", {'info': info[0]})

# def login(request):
#        if request.method == "POST":
#            data = request.POST
#            user = User.objects.create_user(username = data["username"] , last_name = data["last_name"] , email = data["email"] , password = data["password"])
#            user.save()
#        return render(request , "shop/login.html")

# def authorizd(request):
#    if request.method == "POST":
#        data = request.POST
#        user = authenticate(username = data["username"] , email = data["email"] , password = data["password"])
#        if user != None:
#            return render(request , "shop/main.html")
#        else:
#            user = User.objects.create_user(username = data["username"] , email = data["email"] , password = data["password"])
#            user.save()
#            return render(request , "shop/main.html")
#    return render(request , "shop/authorizd.html")


# def auth(request):
#    if request.method == "POST":
#        data = request.POST
#        user = authenticate(username = data["username"] , email = data["email"] , password = data["password"])
#        if user != None:
#            return HttpResponse(str(user))
#        else:
#            new = User(username = data["username"])
#            new = User(email = data["email"])
#            new.set_password(data["password"])
#            new.save()
#            return render(request , "shop/auth.html")
#    return render(request , "shop/auth.html")
