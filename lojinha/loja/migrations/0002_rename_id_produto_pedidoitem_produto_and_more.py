# Generated by Django 4.0.4 on 2022-05-20 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidoitem',
            old_name='id_produto',
            new_name='produto',
        ),
        migrations.AlterField(
            model_name='pedidoitem',
            name='desconto',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pedidoitem',
            name='qtd',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.TextField(),
        ),
    ]
