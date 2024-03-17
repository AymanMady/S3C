# Generated by Django 4.2.8 on 2024-03-17 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_équipe_nombremembres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nom', models.CharField(max_length=255)),
                ('prénom', models.CharField(max_length=255)),
                ('spécialité', models.CharField(choices=[('DSI', 'DSI'), ('RSS', 'RSS'), ('CNM', 'CNM')], max_length=255)),
                ('niveau', models.CharField(choices=[('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('M1', 'M1'), ('M2', 'M2')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Jery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prénom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='niveau',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='prénom',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='spécialité',
        ),
        migrations.AddField(
            model_name='équipe',
            name='nombreMembres',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]