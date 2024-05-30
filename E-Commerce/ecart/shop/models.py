from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='shop/images',default="")
    category=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=200)
    pub_date=models.DateField()
    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70,default='')
    email=models.CharField(max_length=70,default='')
    phone=models.CharField(max_length=70,default='')
    desc=models.CharField(max_length=700,default='')
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_json=models.CharField(max_length=5000)
    email=models.CharField(max_length=70)
    phone=models.CharField(max_length=11)
    name=models.CharField(max_length=50)
    add1=models.CharField(max_length=500)
    add2=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=8)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc