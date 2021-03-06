# Generated by Django 2.2.6 on 2020-03-23 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='branch',
            field=models.CharField(default='NONE', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='destination',
            field=models.CharField(default='NONE', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(default='NONE', max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='works_at',
            field=models.CharField(default='NONE', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='y_o_p',
            field=models.CharField(default='NONE', max_length=20),
        ),
    ]
