from django.db import models
from django.contrib.auth.models import User

# Create your models here.

KEY_TYPE = [
    ("RSA", "RSA Key"),
    ("ECDSA", "ECDSA Key"),
]


class TimeStampedModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-modified"]


class Key(TimeStampedModel):
    """
    Key records table
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, help_text="User initiate the key generation"
    )
    public_key = models.CharField(
        verbose_name="Public Key",
        null=False,
        blank=False,
        help_text="Generated Public Key",
        max_length=1000,
    )
    hsm_label = models.IntegerField(verbose_name="Generated ID/Label Key from softhsm")
    key_type = models.CharField(
        choices=KEY_TYPE,
        blank=False,
        null=False,
        max_length=50,
    )


class Certificate(TimeStampedModel):
    """
    Certificate management TBD
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, help_text="User who create this certificate"
    )

    key = models.ForeignKey(Key, on_delete=models.PROTECT, blank=True, null=True)
