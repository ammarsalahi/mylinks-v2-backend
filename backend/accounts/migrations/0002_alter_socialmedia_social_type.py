# Generated by Django 4.1.2 on 2022-10-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='social_type',
            field=models.CharField(choices=[('telegram', 'telegram'), ('twitter', 'twitter'), ('discord', 'discord'), ('instagram', 'instagram'), ('youtube', 'youtube'), ('github', 'github'), ('linkedin', 'linkedin')], max_length=20, verbose_name='شبکه اجتماعی'),
        ),
    ]
