# Generated by Django 5.0.6 on 2024-06-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_historico_rename_telefone_cliente_cpf_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.AddField(
            model_name='cliente',
            name='apelido',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]