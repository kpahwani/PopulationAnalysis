# Generated by Django 2.0.5 on 2018-06-10 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('fnl_wgt', models.IntegerField(null=True)),
                ('edu_num', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('cap_gain', models.IntegerField(null=True)),
                ('cap_loss', models.IntegerField(null=True)),
                ('hrs_per_week', models.IntegerField(null=True)),
                ('class_grp', models.CharField(choices=[('U', '>50'), ('L', '<=50')], max_length=10, null=True)),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Country')),
                ('edu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Education')),
                ('mar_status_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.MaritalStatus')),
                ('occupation_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Occupation')),
                ('race_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Race')),
                ('relation_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Relationship')),
            ],
        ),
        migrations.CreateModel(
            name='WorkClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='wrk_cls_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.WorkClass'),
        ),
    ]
