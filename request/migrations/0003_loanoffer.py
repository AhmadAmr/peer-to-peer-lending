# Generated by Django 3.2 on 2021-06-19 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0002_auto_20210619_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annual_interest_rate', models.IntegerField()),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Refused', 'Refused')], default='Notselected', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
