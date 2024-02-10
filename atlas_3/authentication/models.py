from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from hashlib import sha1


def profile_pic_path(instance, filename: str) -> str:
    """
    This function computes the path of where to store the profile picture
    :param instance: An instance of AtlasUser based on the current user
    :param filename: original filename
    :return: relative path of profile picture from MEDIA_ROOT
    """
    ext = filename.split('.')[-1]
    return f"profile/{sha1(instance.user.username.encode()).hexdigest()}/{slugify(filename)}.{ext}"


# Create your models here.
class AtlasUser(models.Model):
    class DepartmentNames(models.TextChoices):
        MACHINE_LEARNING = "ML", _("Machine Learning")
        BLOCKCHAIN = "BC", _("Blockchain")
        SOFTWARE_DEVELOPMENT = "SD", _("Software Development")
        QUANT_DEPARTMENT = "QD", _("Quant Department")
        EXTERNAL_RELATIONS = "ER", _("External Relations")
        INTERNAL_AFFAIRS = "IA", _("Internal Affairs")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, choices=DepartmentNames.choices, blank=True)
    profile_pic = models.ImageField(upload_to=profile_pic_path, default='profile/blank_profile.png')

    def __str__(self):
        return f"{self.user.username} in {self.get_department_display()} department"
