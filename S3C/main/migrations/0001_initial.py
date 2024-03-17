# Generated by Django 4.2.6 on 2024-03-17 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prénom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Défi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
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
            name='Jury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prénom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Soumission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lienGit', models.CharField(max_length=255)),
                ('dateSoumission', models.DateTimeField()),
                ('status', models.CharField(choices=[('soumis', 'Soumis'), ('évalué', 'Évalué')], max_length=7)),
                ('défi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.défi')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('motDePasse', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('étudiant', 'Étudiant'), ('organisateur', 'Organisateur'), ('jury', 'Jury')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Évaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('commentaires', models.TextField()),
                ('soumission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.soumission')),
            ],
        ),
        migrations.CreateModel(
            name='Équipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomEquipe', models.CharField(max_length=255)),
                ('nombreMembres', models.IntegerField()),
                ('adjointID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adjoint_teams', to='main.utilisateur')),
                ('leadID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_teams', to='main.utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='soumission',
            name='équipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.équipe'),
        ),
        migrations.CreateModel(
            name='Résultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoreTotal', models.IntegerField()),
                ('équipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.équipe')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('lead', 'Lead'), ('adjoint', 'Adjoint'), ('membre', 'Membre')], max_length=7)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.utilisateur')),
                ('équipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.équipe')),
            ],
        ),
    ]
