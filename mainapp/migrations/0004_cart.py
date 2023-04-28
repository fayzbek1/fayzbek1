# Generated by Django 4.1.7 on 2023-02-24 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_foods_price_alter_foods_price_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.foods')),
            ],
        ),
    ]
