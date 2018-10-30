from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings;
from django.db.models.signals import post_save;
# from django.core.validators import RegexValidator;

class MyUserManager(BaseUserManager):
    def create_user(self,username,first_name,last_name,email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password,first_name=None,last_name=None,):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,first_name=first_name,last_name=last_name,email=email,
            password=password,

        )
        user.is_admin = True
        user.is_staff=True;
        user.save(using=self._db)
        return user

username_validator=r'^[\w\._@]+$';
class MyUser(AbstractBaseUser):
    username=models.CharField(max_length=255,verbose_name="User Name",unique=True);
    first_name=models.CharField(max_length=256,blank=True,null=True);
    last_name=models.CharField(max_length=256,blank=True,null=True);
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False);
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE);
    def __str__(self):
        return self.user.username;
def post_save_user(instance,sender,created,*args,**kwargs):
    if created:
        Profile.objects.create(user=instance);
post_save.connect(post_save_user,sender=settings.AUTH_USER_MODEL);
