# Generated by Django 3.1.3 on 2020-11-21 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_auto_20201117_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', related_query_name='game', to='levelupapi.gamer'),
        ),
    ]