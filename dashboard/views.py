from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import User
from django.contrib import messages
from main import models

@login_required
def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def create_banner(request):
    if request.method == "POST":
        try:
            title = request.POST['title']
            body = request.POST['body']
            models.Banner.objects.create(
                title=title,
                body=body,
            )
            messages.success(request, 'Banner muaffaqiyatli yaratildi')
        except:
            messages.error(request, 'Banner yaratishda xatolik')


    return render(request, 'dashboard/banner/create.html')

@login_required
def list_banner(request):
    try:
        banners = models.Banner.objects.all()
        context = {
            'banners':banners
        }
        messages.success(request, 'muaffaqiyatli bajarildi')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/banner/list.html', context)

@login_required
def banner_detail(request, id):
    try:
        banner = models.Banner.objects.get(id=id)
        context = {
            'banner':banner
        }
        messages.success(request, 'detail muaffaqiyatli bajarildi')
    except:
        messages.error(request, 'nimadur xato ketdi')
    return render(request, 'dashboard/banner/detail.html', context)

@login_required
def banner_edit(request, id):
    banner = models.Banner.objects.get(id=id)
    try:
        if request.method == 'POST':
            banner.title = request.POST['title']
            banner.body = request.POST['body']
            banner.save()
            return redirect('banner_detail', banner.id)
        context = {
            'banner':banner
        }
        messages.success(request, 'edit muaffaqiyatli bajarildi')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/banner/edit.html', context)

@login_required
def banner_delete(request, id):
    try:
        models.Banner.objects.get(id=id).delete()
        messages.success(request, 'delete muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return redirect('list_banner')



# Service
@login_required
def create_service(request):
    if request.method == "POST":
        try:
            name = request.POST['title']
            body = request.POST['body']
            icon = request.POST['file']
            models.Service.objects.create(
                name=name,
                body=body,
                icon=icon,
            )
            messages.success(request, 'Service muvaffaqiyatli yaratildi!')
        except:
            messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/service/create.html')

@login_required
def list_service(request):
    try:
        services = models.Service.objects.all()
        context = {
        'services':services
        }
        messages.success(request, 'list muaffaqiyatli bajarildi')
    except:
        messages.error(request, 'Xato')


    return render(request, 'dashboard/service/list.html', context)


@login_required
def service_detail(request, id):
    try:
        service = models.Service.objects.get(id=id)
        context = {
        'service':service
        }
        messages.success(request, 'detail muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/service/detail.html', context)



@login_required
def service_edit(request, id): 
    try:
        service = models.Service.objects.get(id=id)
        if request.method == 'POST':
            service.name = request.POST['title']
            service.body = request.POST['body']
            service.icon = request.POST['file']
            service.save()
            return redirect('service_detail', service.id)
        context = {
        'service':service
        }
        messages.success(request, 'edit muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato etdi')


    return render(request, 'dashboard/service/edit.html', context)

@login_required
def service_delete(request, id):
    try: 
        models.Service.objects.get(id=id).delete()
        messages.success(request, 'delete muaffaqiyatli')
    except:
        messages.error('nimadur xato ketdi')
        

    return redirect('list_service')




# Aboutus
@login_required
def create_aboutus(request):
    if request.method == "POST":
        try:
            body = request.POST['body']
            models.AboutUs.objects.create(
                body=body,
            )
            messages.success(request, 'Aboutus muvaffaqiyatli yaratildi!')
        except:
            messages.error(request, 'nimadur xato ketdi!')


    return render(request, 'dashboard/aboutus/create.html')


@login_required
def list_aboutus(request):
    try:
        aboutus = models.AboutUs.objects.all()
        context = {
            'aboutus':aboutus
        }
        messages.success(request, 'list muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/aboutus/list.html', context)



@login_required
def  aboutus_detail(request, id):
    try:
        aboutus = models.AboutUs.objects.get(id=id)
        context = {
            'aboutus':aboutus
        }
        messages.success(request, 'detail muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/aboutus/detail.html', context)



@login_required
def aboutus_edit(request, id):
    try:
        aboutus = models.AboutUs.objects.get(id=id)
        if request.method == 'POST':
            aboutus.body = request.POST['body']
            aboutus.save()
            return redirect('aboutus_detail', aboutus.id)
        context = {
            'aboutus':aboutus
        }
        messages.success('reque muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/aboutus/edit.html', context)



@login_required
def aboutus_delete(request, id):
    try:
        models.AboutUs.objects.get(id=id).delete()
        messages.success(request, 'delete muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return redirect('list_aboutus')




# Price
@login_required
def create_price(request):
    if request.method == "POST":
        try:
            title = request.POST['title']
            price = request.POST['price']
            body = request.POST['body']
            models.Price.objects.create(
                title=title,
                price=price,
                body=body,
            )
            messages.success(request, 'Price muvaffaqiyatli yaratildi!')
        except:
            messages.error(request, 'nimadur xato ketdi')

            
    return render(request, 'dashboard/price/create.html')

@login_required
def list_price(request):
    try:
        prices = models.Price.objects.all()
        context = {
            'prices':prices
        }
        messages.success(request, 'price muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/price/list.html', context)



@login_required
def price_edit(request, id):
    try:
        price = models.Price.objects.get(id=id)
        if request.method == 'POST':
            price.title = request.POST['title']
            price.price = request.POST['price']
            price.body = request.POST['body']
            price.save()
            return redirect('price_detail', price.id)
        context = {
            'price':price
        }
        messages.success(request, 'price muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/price/edit.html', context)


@login_required
def price_detail(request, id):
    try:
        price = models.Price.objects.get(id=id)
        context = {
            'price':price
        }
        messages.success(request, 'detail muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/price/detail.html', context)



@login_required
def price_delete(request, id):
    try:
        models.Price.objects.get(id=id).delete()
        messages.success(request, 'delete muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')

    
    return redirect('list_price')







# Contact
@login_required
def contact_detail(request, id):
    try:
        contact = models.Contact.objects.get(id=id)
        context = {
            'contact':contact
        }
        messages.success(request, 'detail muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/contact/detail.html', context)



@login_required
def contact_edit(request, id):
    try:
        contact = models.Contact.objects.get(id=id)
        if request.method == 'POST':
            contact.name = request.POST['name']
            contact.phone = request.POST['phone']
            contact.email = request.POST['email']
            contact.body = request.POST['body']
            contact.is_show = request.POST['is_show']
            contact.created_at = request.POST['created_at']
            contact.save()
            return redirect('contact_detail', contact.id)
        context = {
            'contact':contact
        }
        messages.success(request, 'edit muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')


    return render(request, 'dashboard/contact/edit.html', context)


@login_required
def contact_list(request):
    try:
        contacts = models.Contact.objects.all()
        context = {
            'contacts':contacts
        }
        messages.success(request, 'list muaffaqiyatli')
    except:
        messages.error(request, 'nimadur xato ketdi')

        
    return render(request, 'dashboard/contact/list.html', context)





# Register 
def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            password_confirm = request.POST['password_confirm']
            if password == password_confirm:
                User.objects.create_user(
                    username = username,
                    password = password
            )
            messages.success(request, 'Registratsiyadan muvaffaqiyatli o`tdingiz!')
        except:
            messages.error(request, 'nimadur xato ketdi')

    return render(request, 'dashboard/auth/register.html')



def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    
        user = authenticate(
            username = username, 
            password = password
            )
        if user:
            login(request, user)
            return redirect('dashboard:index')
        else:
            ...

    return render(request, 'dashboard/auth/login.html')



def log_out(request):
    logout(request)
    return redirect('main:index')


# QUERRY
def query(request):
    q = request.GET['q']
    baners = models.Banner.objects.filter(title=q)
    services = models.Service.objects.filter(name=q)
    price = models.Price.objects.filter(title=q)
    contact = models.Contact.objects.filter(name=q)
    context = {
        'baners': baners,
        'services': services,
        'price': price,
        'contact': contact,
    }
    return render(request, 'dashboard/query.html', context)