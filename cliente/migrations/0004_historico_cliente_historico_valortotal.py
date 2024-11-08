# Generated by Django 5.0.6 on 2024-06-14 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_remove_cliente_email_cliente_apelido'),
    ]

    operations = [
        migrations.AddField(
            model_name='historico',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historico',
            name='valorTotal',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
