# Generated by Django 3.0.3 on 2020-04-23 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrecords',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='first_App.Webpage'),
        ),
        migrations.AddField(
            model_name='webpage',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='first_App.Topic'),
        ),
    ]
