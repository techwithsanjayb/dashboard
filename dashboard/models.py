from django.db import models


# Create your models here.
class Domain_Information(models.Model):
    Eng_URL = models.URLField(max_length=50, blank=True)
    Eng_Status = models.BooleanField(default=False)
    Eng_Content = models.CharField(max_length=20, blank=True)
    Hindi_URL = models.URLField(max_length=50, blank=True)
    Hindi_Status = models.BooleanField(default=False)
    Hindi_Content = models.CharField(max_length=20, blank=True)
    Marathi_URL = models.URLField(max_length=50, blank=True)
    Marathi_Status = models.BooleanField(default=False)
    Marathi_Content = models.CharField(max_length=20, blank=True)
    Bengali_URL = models.URLField(max_length=50, blank=True)
    Bengali_Status = models.BooleanField(default=False)
    Bengali_Content = models.CharField(max_length=20, blank=True)
    Kannada_URL = models.URLField(max_length=50, blank=True)
    Kannada_Status = models.BooleanField(default=False)
    Kannada_Content = models.CharField(max_length=20, blank=True)
    Malayalam_URL = models.URLField(max_length=50, blank=True)
    Malayalam_Status = models.BooleanField(default=False)
    Malayalam_Content = models.CharField(max_length=20, blank=True)
    Manipuri_URL = models.URLField(max_length=50, blank=True)
    Manipuri_Status = models.BooleanField(default=False)
    Manipuri_Content = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = 'Domain Information'

    def __str__(self):
        return self.Eng_URL
