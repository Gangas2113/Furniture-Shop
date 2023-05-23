from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class contact(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    message=models.TextField()
    class Meta:
        db_table="contact"

class blog(models.Model):
    title=models.CharField(max_length=100)
    description=HTMLField()
    photo=models.ImageField(upload_to='blog/')
    postby=models.CharField(max_length=50)
    poston=models.DateField()
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.title
    

class faq(models.Model):
    question=models.TextField()
    answer=models.TextField()
    class Meta:
        db_table="faq"
    def __str__(self):
        return self.question
    

class category(models.Model):
    title=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='category/')
    class Meta:
        db_table="category"
    def __str__(self):
        return self.title

MYTAG=(
    ('bestselling','bestselling'),
    ('latest','latest'),
    ('new','new'),
)
class products(models.Model):
    title=models.CharField(max_length=200)
    rating=models.FloatField(default="1.1",blank="true",null="true")
    sellingprice=models.FloatField()
    material=models.CharField(max_length=200)
    description=HTMLField()
    photo=models.ImageField(upload_to='product/',default="")
    photo1=models.ImageField(upload_to='product/',default="")
    photo2=models.ImageField(upload_to='product/',default="")
    size=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    style=models.CharField(max_length=100)
    categoryid=models.ForeignKey(category,on_delete=models.CASCADE)
    tag=models.CharField(max_length=50,choices=MYTAG)
    class Meta:
        db_table="product"
    def __str__(self):
        return self.title


class gallery(models.Model):
    photo=models.ImageField(upload_to='gallery/')
    class Meta:
        db_table="gallery"




   

class review(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    
    message=models.CharField(max_length=1000)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    proid=models.ForeignKey(products,on_delete=models.CASCADE)    
    class Meta:
        db_table="review"











