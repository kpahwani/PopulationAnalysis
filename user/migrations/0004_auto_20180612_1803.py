# Generated by Django 2.0.6 on 2018-06-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180610_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='class_grp',
            field=models.CharField(choices=[('U', '>50K'), ('L', '<=50K')], max_length=10, null=True),
        ),
    ]