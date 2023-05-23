from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from shop.forms import *
from django.contrib.auth import login
from orders.models import *
from cart.forms import CartAddProductForm
# Create your views here.
class aboutview(TemplateView):
    template_name="about.html"
class bootview(TemplateView):
    template_name="boot1.html"
class startbootview(TemplateView):
    template_name="bootstrap.html"
class forestview(TemplateView):
    template_name="forest.html"
class formview(TemplateView):
    template_name="forms.html"
class furnitureview(TemplateView):
    template_name="furniture.html"
class extraview(TemplateView):
    template_name="extra.html"
class contactview(TemplateView):
    template_name="contact.html"
class aboutusview(TemplateView):
    template_name="aboutus.html"
class reviewsview(TemplateView):
    template_name="reviews.html"

def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/furniture/')  
    else:
        form=contactform()
    return render(request,"contact.html",{'form':form})


def blogview(request):
    blg=blog.objects.all().order_by('-poston')
    return render(request,"blogs.html",{'blg':blg})

def blogdetailview(request,id):
    b=blog.objects.get(id=id)
    return render(request,"blogdetail.html",{'b':b})

def faqview(request):
    fraq=faq.objects.all()
    return render(request,"faq.html",{'fraq':fraq})

def signup(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("/furniture/")
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})

def categoryview(request):
    catg=category.objects.all()
    return render(request,"category.html",{'catg':catg})


def productview(request,id):
    p=products.objects.filter(categoryid_id=id).order_by('-id')
    return render(request,"product.html",{'p':p})

def productdetailview(request,id):
    p=products.objects.get(id=id)
    cart_add_product_form=CartAddProductForm()
    return render(request,"productdetail.html",{'p':p,'cart_add_product_form':cart_add_product_form})

def searchview(request):
    srh=request.GET['searchbox']
    p=products.objects.filter(title__icontains=srh)
    context={'p':p}
    return render(request, 'search-result.html', context)


    
def galleryview(request):
    gall=gallery.objects.all()
    return render(request,"gallery.html",{'gall':gall})

def myorderview(request):
    o=OrderItem.objects.select_related('order').filter(order__userid=request.user.id)
    return render(request,"myorder.html",{'o':o})

def insertreview(request):
    if request.method=='POST':
        form=reviewform(request.POST)
        next=request.POST.get('next')
        if form.is_valid():
            form.save()
            return redirect(next)  
    else:
        form=reviewform()
    return render(request,"productdetail.html",{'form':form})



    