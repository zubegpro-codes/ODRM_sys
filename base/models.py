from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,)
    bio = models.TextField(blank=True)
    nin = models.CharField(max_length=11, null=True)
    phoneNo = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=250, null=True)
    avatar = models.ImageField(null=True, upload_to='images/', default='avatar.svg')
    updated = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return self.username  # Display the name of the user in the admin panel



class Category(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name



class Report(models.Model):
    user = models.ForeignKey(CustomUser, related_name='reports', on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True)
    Rimg = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.TextField(null=False, blank=True)
    locate = models.CharField(max_length=250,null=False, blank=False)
    contributors = models.ManyToManyField(CustomUser, related_name = 'participants', blank=True )
    status = models.CharField(max_length=20, choices=[('unread', 'Unread'), ('in-progress','In-Progress'), ('successful', 'Successful')],
                              default='unread')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated', 'created']
    def __str__(self):
        return self.title
    

class Location(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True,null=True)
    post = models.ForeignKey(Report, on_delete=models.SET_NULL, blank=True, null=True)
    presentAddres =models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.presentAddres


class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


