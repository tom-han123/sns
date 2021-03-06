# Generated by Django 4.0.2 on 2022-02-16 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='B_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('base_prize', models.IntegerField(default=0)),
                ('prize', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.CharField(max_length=200, null=True)),
                ('bore_stroke', models.CharField(max_length=200, null=True)),
                ('capacity', models.CharField(max_length=200, null=True)),
                ('rated_output', models.CharField(max_length=200, null=True)),
                ('torque', models.CharField(max_length=200, null=True)),
                ('compression', models.CharField(max_length=200, null=True)),
                ('mixture_control', models.CharField(max_length=200, null=True)),
                ('emission_control', models.CharField(max_length=200, null=True)),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.b_models')),
            ],
        ),
        migrations.AddField(
            model_name='b_models',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.types'),
        ),
    ]
