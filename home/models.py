from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    gggfgf = models.BigIntegerField(null=True, blank=True,)
    kjuyiu = models.BigIntegerField(null=True, blank=True,)
    uyiuyi = models.BigIntegerField(null=True, blank=True,)
    jhgjh = models.BigIntegerField(null=True, blank=True,)
    jhgj = models.BigIntegerField(null=True, blank=True,)
    nbhjg = models.BigIntegerField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
