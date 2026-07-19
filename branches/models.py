from django.db import models
from companies.models import Company


class Branch(models.Model):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="branches"
    )

    name = models.CharField(max_length=200)

    code = models.CharField(
        max_length=20,
        unique=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
    