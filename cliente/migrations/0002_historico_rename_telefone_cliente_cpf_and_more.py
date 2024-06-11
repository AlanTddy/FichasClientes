# Generated by Django 5.0.6 on 2024-06-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dataPagamento', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='telefone',
            new_name='cpf',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='pago',
        ),
    ]
