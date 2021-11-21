from django.db import models
import os

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.owner}-{instance.start_date}-{instance.end_date}{ext}"
    return f"walls/{final_name}"
class WallManager(models.Manager):
    def get_active_wall(self):
        return self.get_queryset().filter(active=True)

class Wall(models.Model):
    owner = models.CharField(max_length=40,verbose_name='صاحب')
    location = models.TextField(verbose_name='مکان')
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(verbose_name='تاریخ پایان')
    space_count = models.IntegerField(null=True,verbose_name='فضای خالی')
    image = models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name='تصویر')
    price = models.IntegerField(default=0,verbose_name='هزینه اجاره')
    active = models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
    availabale = models.BooleanField(default=True,verbose_name='اجاره شده')
    creator_id = models.IntegerField(default=0,null=False,verbose_name='شناسه کاربر سازنده')

    objects = WallManager()

    class Meta:
        verbose_name_plural = 'دیوارها'
        verbose_name = 'دیوار'


    def __str__(self):
        return self.location