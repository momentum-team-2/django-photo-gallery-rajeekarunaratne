# Generated by Django 3.0.8 on 2020-08-05 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover_for', to='core.Photo'),
        ),
    ]
