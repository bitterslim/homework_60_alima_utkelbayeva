from django.db import models

class Order(models.Model):
    product = models.ForeignKey( verbose_name='Product',  to='webapp.Product', related_name='product', on_delete=models.CASCADE),
    user_name = models.CharField(verbose_name='Username',max_length=100,null=False,blank=False)
    phone = models.CharField(verbose_name='Phone',max_length=20, null=False, blank=False)
    address = models.CharField(verbose_name='Address', max_length=200,null=False,blank=False)
