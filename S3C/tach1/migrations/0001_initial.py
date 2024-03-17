# Generated by Django 4.2.8 on 2024-03-17 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prénom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('motDePasse', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('étudiant', 'Étudiant'), ('organisateur', 'Organisateur'), ('jury', 'Jury')], max_length=12)),
                ('spécialité', models.CharField(max_length=255)),
                ('niveau', models.CharField(choices=[('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('M1', 'M1'), ('M2', 'M2')], max_length=3)),
            ],
        ),
    ]
