from django.db import models

class Project(models.Model):
    title=models.CharField(
        max_length=200,
        verbose_name="نام پروژه"
    )

    description=models.TextField(
        verbose_name="توضیحات"
    )
    images=models.ManyToManyField(
        'demo.image',
        verbose_name='تصاویر'
    )
    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name="ایجاد"
    )

    updated_at=models.DateTimeField(
        auto_now=True,
        verbose_name="بروز رسانی"
    )

    url=models.URLField(
        blank=True,
        verbose_name="آدرس پروژه"
    )

    repo_url=models.URLField(
        blank=True,
        verbose_name="آدرس ریپوزیتوری"
    )

    user =models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='projects',
        verbose_name="کاربر"
    )
    
    class Meta:
        verbose_name="پروژه"
        verbose_name_plural="پروژه ها"

    def __str__(self):
        return self.title
