from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group
from django.contrib.auth.models import PermissionsMixin,Permission
from django.forms import ValidationError


class UserAccountManager(BaseUserManager):
    use_in_migrations = True
    

    def create_user(self, username,email, password=None):
        if not username:
            raise ValueError("Username invalid")
        if not email:
            raise ValueError("Email invalid")

        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password):
        user = self.create_user(username=username,email=email,password=password)
        # user.is_active = True
        # user.is_admin = True
        # user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
# python manage.py dumpdata main.user --output main/fixtures/users.test.json
class User(AbstractBaseUser, PermissionsMixin):
    """ BmUser model """
    username=models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=250, unique=True,null=True,blank=True)
    password = models.CharField(max_length=250,null=True,blank=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now_add=True,null=True,blank=True)
    is_staff = models.BooleanField(default=True,null=True,blank=True)    # admin
    is_enabled = models.BooleanField(default=True,null=True,blank=True)
    is_superuser = models.BooleanField(default=True,null=True,blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password',]

    objects = UserAccountManager()

    def __str__(self):
        return f"{self.email}"
  
    
    def has_module_perms(self, app_label):
        return True

    class Meta:
        ordering = ['id']

#  python manage.py dumpdata main.Category --output main/fixtures/Category.static.json
class Category(models.Model):
    name=models.CharField(max_length=100)
    name_ar=models.CharField(max_length=100)
    index=models.IntegerField(default=1)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Categories"


def upload_program(obj,file_name):
    return f'programs/{obj.name}.png'

#  python manage.py dumpdata main.Program --output main/fixtures/Program.static.json
class Program(models.Model):
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    name=models.CharField(max_length=100)
    name_ar=models.CharField(max_length=100)
    index=models.IntegerField(default=1)
    is_enabled = models.BooleanField(default=True)
    description=models.TextField()
    description_ar=models.TextField()
    image=models.ImageField(upload_to=upload_program)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Programs"
        


class ContactUs(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"