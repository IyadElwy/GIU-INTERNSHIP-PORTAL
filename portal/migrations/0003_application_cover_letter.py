# Generated by Django 4.0 on 2022-04-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_progressreport_application_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='cover_letter',
            field=models.TextField(default='My cover letter'),
            preserve_default=False,
        ),
    ]
