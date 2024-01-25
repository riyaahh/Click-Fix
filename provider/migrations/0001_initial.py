# Generated by Django 4.2.7 on 2024-01-23 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='provider',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=30)),
                ('pcontactno', models.CharField(max_length=12)),
                ('pemail', models.CharField(max_length=40)),
                ('pstatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('stype', models.CharField(max_length=20)),
                ('sprice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='providerpaymentdetails',
            fields=[
                ('payid', models.IntegerField(primary_key=True, serialize=False)),
                ('method', models.CharField(max_length=20)),
                ('appid', models.IntegerField()),
                ('amount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.provider')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.service')),
            ],
        ),
        migrations.AddField(
            model_name='provider',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.service'),
        ),
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('appid', models.IntegerField(primary_key=True, serialize=False)),
                ('cid', models.IntegerField()),
                ('cpayid', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.provider')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.service')),
            ],
        ),
    ]