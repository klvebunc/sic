# Generated by Django 3.1.3 on 2021-07-06 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sic', '0024_auto_20210706_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='hat',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='hats', to='sic.user'),
            preserve_default=False,
        ),
    ]
