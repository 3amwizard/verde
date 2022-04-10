# Generated by Django 3.2.9 on 2022-04-06 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=36)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=72)),
                ('service', models.CharField(choices=[('Verde People', 'Verde People'), ('Verde Fleet', 'Verde Fleet'), ('Verde Leave', 'Verde Leave'), ('Verde Gift Reg', 'Verde Gift Reg'), ('Verde Claims', 'Verde Claims'), ('Verde ELC', 'Verde ELC'), ('Verde Policy', 'Verde Policy')], max_length=72)),
                ('size', models.CharField(choices=[('1-10', '1-10'), ('11-50', '11-50'), ('51-100', '51-100'), ('101-500', '101-500'), ('501 -1000', '501-1000'), ('Over 1001', 'Over 1001')], max_length=72)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]