# Generated by Django 2.0.5 on 2021-08-27 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Entrez votre nom SVP')),
                ('serie', models.CharField(choices=[('A', 'A'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=50, verbose_name='entrez serie')),
                ('nbfois', models.IntegerField(choices=[('A', 2), ('C', 3), ('D', 4)], verbose_name='Combien de fois avez vous manquez votre examen ?')),
                ('age', models.IntegerField(verbose_name='Entrez votre age ')),
                ('score', models.IntegerField()),
            ],
        ),
    ]
