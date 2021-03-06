# Generated by Django 3.0.14 on 2022-02-18 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_auto_20220217_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='internshipbranch', to='base_app.branch_registration'),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='password',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendanceuser', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='create_team',
            name='trainer',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='department',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='departmentbranch', to='base_app.branch_registration'),
        ),
        migrations.AlterField(
            model_name='designation',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='designationbranch', to='base_app.branch_registration'),
        ),
        migrations.AlterField(
            model_name='extracurricular',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='extracurricularuser', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='reg_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='from_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='to_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='leaveuser', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='project',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectbranch', to='base_app.branch_registration'),
        ),
        migrations.AlterField(
            model_name='project',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectdepartment', to='base_app.branch_registration'),
        ),
        migrations.AlterField(
            model_name='project',
            name='enddate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='startdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectuser', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='project_taskassign',
            name='enddate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project_taskassign',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassignproject', to='base_app.project'),
        ),
        migrations.AlterField(
            model_name='project_taskassign',
            name='startdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project_taskassign',
            name='submitted_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project_taskassign',
            name='tl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassigntl', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='project_taskassign',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassignuser', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='qualificationuser', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='reported_issue',
            name='reported_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reported_issue',
            name='reported_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reported_issuereported_to', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='reported_issue',
            name='reporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reported_issuereporter', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='test_status',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='test_status',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statusproject', to='base_app.project'),
        ),
        migrations.AlterField(
            model_name='test_status',
            name='taskname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statustaskname', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='test_status',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statususer', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='test_status',
            name='workdone',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tester_status',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tester_status',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statusproject', to='base_app.project'),
        ),
        migrations.AlterField(
            model_name='tester_status',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statustask', to='base_app.project_taskassign'),
        ),
        migrations.AlterField(
            model_name='tester_status',
            name='tester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statustester', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='tester_status',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statususer', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='enddate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='startdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='topicteam', to='base_app.create_team'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='topictrainer', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='trainer_task',
            name='enddate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='trainer_task',
            name='startdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='trainer_task',
            name='trainee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trainer_tasktrainee', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='trainer_task',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trainer_tasktrainer', to='base_app.user_registration'),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationbranch', to='base_app.branch_registration'),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='dateofbirth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationdepartment', to='base_app.department'),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationdesignation', to='base_app.designation'),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='enddate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='joiningdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='startdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationteam', to='base_app.create_team'),
        ),
    ]
