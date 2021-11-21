from django.db import models
import os
from wall.models import Wall
from art_artist.models import Art
import qrcode


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}-{instance.start_date}-{instance.end_date}{ext}"
    return f"reservs/{final_name}"

def upload_qrcode_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Qrcode/{instance.title}-{instance.start_date}-{instance.end_date}{ext}"
    return f"reservs/{final_name}"

class ReservManager(models.Manager):
    def get_active_reserv(self):
        return self.get_queryset().filter(active=True)

    def get_reserv_id(self, reserv_id):
        qs = self.get_queryset().filter(id=reserv_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class Reserv(models.Model):
    title = models.CharField(max_length=40,null=True,verbose_name='نام')
    subject = models.CharField(max_length=40,null=True,verbose_name='موضوع')
    start_date = models.DateField(null=True,verbose_name='تاریخ شروع')
    end_date = models.DateField(null=True,verbose_name='تاریخ پایان')
    image = models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name='تصویر')
    about = models.TextField(null=True,verbose_name='درباره')
    active = models.BooleanField(default=False,verbose_name='فعال/غیرفعال',editable=True)
    price = models.IntegerField(default=0,verbose_name='هزینه رزرو')
    art = models.ManyToManyField(Art,verbose_name='انتخاب تصویر')
    wall = models.ManyToManyField(Wall,verbose_name='انتخاب دیوار')
    qrcode_image = models.ImageField(upload_to=upload_qrcode_image_path,null=True,blank=True,verbose_name='کداسکن')

    objects = ReservManager()

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزوها'

    def __str__(self):
        return self.title