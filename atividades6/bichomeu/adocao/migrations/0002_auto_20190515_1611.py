# Generated by Django 2.2.1 on 2019-05-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='cor',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='doador',
            name='cpf',
            field=models.CharField(default='', max_length=15),
        ),
    ]
