# Generated by Django 4.2.6 on 2024-05-17 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='images',
            field=models.ImageField(upload_to='website/Project_images/'),
        ),
    ]
