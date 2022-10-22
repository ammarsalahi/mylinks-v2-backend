from django.db import models


class Image(models.Model):
    picture=models.ImageField(
        upload_to="project-images/",
        verbose_name='تصویر'
    )

    class Meta:
        verbose_name="تصویر"
        verbose_name_plural="تصاویر"
    def get_url(self):
        return self.picture.url