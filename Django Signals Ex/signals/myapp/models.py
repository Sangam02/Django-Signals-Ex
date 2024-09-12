# Question 1 :  By default are django signals executed synchronously or asynchronously?
# Answer 1 : The short answer is no, Django signals are not inherently asynchronous.

from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return {self.title}
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username




# Question 2: Do django signals run in the same thread as the caller?
# Answer 2:Yes, Django signals run in the same thread as the caller. This means that when a signal is emitted, the connected signal handlers execute synchronously in the same thread and process that triggered the signal.



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# Question 3: By default do django signals run in the same database transaction as the caller?
# Answer 3: Yes, by default, Django signals run in the same database transaction as the caller. This means that any changes made by the signal handler will be part of the same database transaction that triggered the signal. If the transaction is rolled back, the changes made by the signal handler will also be rolled back.


class AuditLog(models.Model):
    product_name = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)