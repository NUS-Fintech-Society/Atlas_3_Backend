from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


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

    def __str__(self):
        return f"{self.user.username} in {self.get_department_display()} department"
