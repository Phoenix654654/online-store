from django.db import models

# class Category(models.Model):
#     title = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.title
    

# class Product(models.Model):
#     title = models.CharField(max_length=50, blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     quantity = models.IntegerField(null=False, blank=False)
#     image1 = models.ImageField(upload_to='media/product_image/')
#     image2 = models.ImageField(upload_to='media/product_image/', null=True, blank=True)
#     image3 = models.ImageField(upload_to='media/product_image/', null=True, blank=True)
#     image4 = models.ImageField(upload_to='media/product_image/', null=True, blank=True)
#     image5 = models.ImageField(upload_to='media/product_image/', null=True, blank=True)
#     image6 = models.ImageField(upload_to='media/product_image/', null=True, blank=True)
#     in_stock = models.BooleanField(default=True)
#     discount = models.IntegerField(null=True, blank=True)

#     display = models.FloatField(null=True, blank=True)
#     processor = models.CharField(max_length=255, null=True, blank=True)
#     video_card = models.CharField(max_length=255, null=True, blank=True)
#     ram = models.IntegerField(null=True, blank=True)
#     color = models.CharField(max_length=255, null=True, blank=True)

#     connection_type = models.CharField(max_length=255, null=True, blank=True)
#     design = models.CharField(max_length=255, null=True, blank=True)
#     wire_length = models.IntegerField(null=True, blank=True)
#     equipment = models.CharField(max_length=255, null=True, blank=True)
#     type = models.CharField(max_length=255, null=True, blank=True)
#     charging_type = models.CharField(max_length=255, null=True, blank=True)
#     material = models.CharField(max_length=255, null=True, blank=True)
#     model = models.CharField(max_length=255, null=True, blank=True)
#     capacity = models.IntegerField(null=True, blank=True)
#     fastening = models.CharField(max_length=255, null=True, blank=True)

#     width = models.IntegerField(null=True, blank=True)
#     length = models.IntegerField(null=True, blank=True)
#     height = models.IntegerField(null=True, blank=True)
    
#     is_active = models.BooleanField(default=True)
