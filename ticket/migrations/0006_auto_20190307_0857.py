# Generated by Django 2.1.7 on 2019-03-07 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_salon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='subservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.Service'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='logo',
            field=models.ImageField(blank=True, default='/static/ticket/images/logo/logo_sbs.png', null=True, upload_to=''),
        ),
    ]
