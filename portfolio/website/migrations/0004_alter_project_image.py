# Generated by Django 4.1.3 on 2022-12-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(height_field=100, upload_to='media/', width_field=100),
        ),
    ]
