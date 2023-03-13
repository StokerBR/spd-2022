# Generated by Django 4.1.3 on 2022-12-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
                ('dt_nasc', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('lougradouro', models.CharField(max_length=60)),
                ('numero', models.IntegerField()),
                ('setor', models.CharField(max_length=40)),
                ('cidade', models.CharField(max_length=40)),
                ('uf', models.CharField(max_length=25)),
            ],
        ),
    ]