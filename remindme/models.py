from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser


class ReminderUser(AbstractBaseUser):
    username = models.CharField(max_length=256, unique=True, db_index=True)
    name = models.CharField(max_length=256)
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True, db_index=True,)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def is_staff(self):
        """Special django method to detect admin privileges."""
        return self.is_admin

    def is_superuser(self):
        """Special django method to detect admin privileges."""
        return self.is_admin

    def get_full_name(self):
        """Special django method to determine name of user (including for admin)."""
        return self.get_short_name()

    def has_perm(self, perm, obj=None):
        """Special django method for privileges (only used for admin)."""
        return self.is_admin

    def has_module_perms(self, app_label):
        """Special django method for privileges (only used for admin)."""
        return self.is_admin

    def get_short_name(self):
        """Special django method to determine name of user (including for admin)."""
        if self.name is None or self.name == "":
            return self.email
        else:
            return self.name

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [username, email]



class Reminder(models.Model):
    user = models.ForeignKey(ReminderUser)
    description = models.CharField(max_length=256)
    date_and_time = models.DateTimeField()
    sent = models.BooleanField(default=False)
