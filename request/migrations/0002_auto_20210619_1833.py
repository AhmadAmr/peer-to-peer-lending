# Generated by Django 3.2 on 2021-06-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='loan_period',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Funded', 'Funded'), ('Completed', 'Completed')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='loanrequest',
            name='what_for',
            field=models.CharField(choices=[('RATE', 'RATE')], max_length=50),
        ),
    ]