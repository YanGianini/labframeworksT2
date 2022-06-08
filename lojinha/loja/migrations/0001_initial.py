# Generated by Django 4.0.4 on 2022-05-20 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ativo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('qtd_estoque', models.IntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagem', models.CharField(max_length=255)),
                ('ativo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd', models.IntegerField()),
                ('desconto', models.IntegerField()),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.produto')),
            ],
        ),
    ]
