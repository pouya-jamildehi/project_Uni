import os
from django.db import models

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.paintistname}-{instance.title}{ext}"
    return f"arts/{final_name}"

class ArtManager(models.Manager):
    def get_active_art(self):
        return self.get_queryset().filter(active=True)

    def get_art_id(self, art_id):
        qs = self.get_queryset().filter(id=art_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

class Art(models.Model):
    title = models.CharField(max_length=40,verbose_name='عنوان')
    paintistname = models.CharField(max_length=40, null=True,verbose_name='هنرمند')
    subject = models.CharField(max_length=40,verbose_name='موضوع')
    about = models.TextField(verbose_name='توضیحات')
    date = models.DateField(verbose_name='تاریخ ایجاد')
    material = models.CharField(max_length=40,verbose_name='متریال')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,verbose_name='تصویر')
    active = models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
    availabale = models.BooleanField(default=True, verbose_name='دردسترس / دردسترس نیست')
    creator_id = models.IntegerField(default=0,null=False,verbose_name='شناسه کاربر سازده')

    objects = ArtManager()

    class Meta:
        verbose_name = 'هنر'
        verbose_name_plural = 'هنرها'

    def __str__(self):
        return self.title