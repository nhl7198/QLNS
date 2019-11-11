# Generated by Django 2.1 on 2019-11-11 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QuanLyNhaSach', '0021_auto_20181216_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='extend_info', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]