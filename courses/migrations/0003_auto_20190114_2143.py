# Generated by Django 2.1.5 on 2019-01-14 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_step'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['order']},
        ),
    ]
