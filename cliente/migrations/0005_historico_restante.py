# Generated by Django 5.0.6 on 2024-06-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_historico_cliente_historico_valortotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='historico',
            name='restante',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
