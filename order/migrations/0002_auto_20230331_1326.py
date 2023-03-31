# Generated by Django 3.2.18 on 2023-03-31 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrengthLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='coffeebean',
            name='strength_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='order.strengthlevel'),
        ),
    ]