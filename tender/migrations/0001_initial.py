# Generated by Django 5.0.2 on 2024-03-08 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_no', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('assigned', 'Assigned'), ('available', 'Available'), ('expired', 'Expired')], default='available', max_length=20)),
                ('due_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tender.category')),
            ],
        ),
        migrations.CreateModel(
            name='TenderDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='tender_documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tender.tender')),
            ],
        ),
    ]
