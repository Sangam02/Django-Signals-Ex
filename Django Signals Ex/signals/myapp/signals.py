# question 1

from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import BlogPost,  UserProfile
from django.utils.text import slugify


@receiver(pre_save, sender=BlogPost)
def slugify_title(sender, instance, **kwargs):
    if not instance.slug:  
        instance.slug = slugify(instance.title)  


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  
        UserProfile.objects.create(user=instance)




# question 2


from .models import Product
import threading

@receiver(post_save, sender=Product)
def product_saved(sender, instance, **kwargs):
    print(f"Product '{instance.name}' has been saved.")
    print(f"Handler running in thread: {threading.current_thread().name}")



# question 3


from django.db import transaction
from .models import AuditLog

@receiver(post_save, sender=Product)
def log_product_save(sender, instance, **kwargs):
    AuditLog.objects.create(product_name=instance.name, action="Product saved")
    current_transaction = transaction.get_connection().in_atomic_block
    print(f"In atomic block: {current_transaction}")