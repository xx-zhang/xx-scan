# Generated by Django 2.1.7 on 2019-05-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanscript',
            name='args',
            field=models.CharField(blank=True, max_length=155, verbose_name='脚本填充参数'),
        ),
    ]