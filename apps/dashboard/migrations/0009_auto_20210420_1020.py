# Generated by Django 3.1 on 2021-04-20 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20210420_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='expire_date',
        ),
        migrations.CreateModel(
            name='AssignAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_on', models.DateTimeField(auto_now_add=True)),
                ('expire_on', models.DateTimeField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.asset')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.employee')),
            ],
        ),
    ]