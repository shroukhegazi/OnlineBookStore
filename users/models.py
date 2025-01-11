from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, username, email, name,password=None):
        if not username:
            raise TypeError("user must have username")
        if not name:
            raise TypeError("user must have name")
        if not email:
            raise TypeError("user must have email")
        if not password:
            raise TypeError("user must have password")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, name,password=None):
        if not username:
            raise TypeError("superuser must have username")
        if not email:
            raise TypeError("superuser must have email")
        if not name:
            raise TypeError("superuser must have name")        
        if not password:
            raise TypeError("superuser must have password")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("User Full Name"), max_length=155, default="")
    email = models.EmailField(_("Email"), max_length=155, unique=True)
    username = models.CharField(
        _("Username"), max_length=155, unique=True, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "email"]

    objects = UserManager()
