# Generated by Django 5.0.6 on 2024-05-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_homecontent_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='static/img/'),
        ),
    ]
