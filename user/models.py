# User models

# Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    """
    Profile model

    Proxy Model that extends the base data with other information.
    """
    
    # Relationship with the user table
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # extended fields

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='user/pictures',
        blank=True,
        null=True
    )

    # time
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(User, related_name='blogpost_like')


    def __str__(self):
        """Return username"""
        return self.user.username

    def number_of_likes(self):
        return self.likes.count()