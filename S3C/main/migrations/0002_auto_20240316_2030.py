# Generated by Django 2.2.22 on 2024-03-16 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='spécialité',
            field=models.CharField(choices=[('DSI', 'DSI'), ('RSS', 'RSS'), ('CNM', 'CNM')], max_length=255),
        ),
    ]