from enum import unique
from django.db import models

socials=[
    ('telegram','تلگرام'),
    ('twitter','توییتر'),
    ('discord','دیسکورد'),
    ('instagram','اینستاگرام'),
    ('youtube','یوتیوب'),
    ('github','گیت هاب'),
    ('linkedin','لینکدین'),
]
class SocialMedia(models.Model):

    social_type=models.CharField(
        max_length=20,
        verbose_name="شبکه اجتماعی",
        choices=socials
    )

    username=models.CharField(
        max_length=20,
        verbose_name="نام کاربری",
        unique=True
    )
    user =models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='socials',
        verbose_name="کاربر"
    )

    class Meta:
        verbose_name="شبکه اجتماعی"
        verbose_name_plural="شبکه های اجتماعی"

    def __str__(self) -> str:
        return '%s-%s'.format(self.social_type,self.username)    

