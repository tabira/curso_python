# Generated by Django 2.2.1 on 2019-05-15 19:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('porte', models.CharField(choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.IntegerField(default=0)),
                ('especie', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('doador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adocao.Doador')),
                ('raca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adocao.Raca')),
            ],
        ),
        migrations.CreateModel(
            name='Adocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adocao.Animal')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adocao.Cliente')),
            ],
        ),
    ]
