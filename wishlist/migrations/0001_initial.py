# Generated by Django 3.2.18 on 2023-04-22 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accessories', '0002_auto_20230401_1312'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accessory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accessories.accessory')),
                ('CoffeeBean', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.coffeebean')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
