# Generated by Django 3.1.7 on 2021-03-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='userPost',
            field=models.CharField(choices=[('CG', 'CG'), ('Coordinator', 'Coordinator'), ('Organiser', 'Organiser')], default='CG', max_length=30),
        ),
    ]