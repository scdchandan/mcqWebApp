# Generated by Django 3.0.3 on 2020-04-23 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_App', '0002_auto_20200423_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessrecords',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_App.Webpage'),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_App.Topic'),
        ),
    ]
