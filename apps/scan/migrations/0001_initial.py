# Generated by Django 2.1.7 on 2019-05-23 17:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='系统部件名称')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('type', models.CharField(default='CommonHost', max_length=128, verbose_name='系统部件的类型')),
                ('os', models.CharField(default='Linux', max_length=128, verbose_name='操作系统')),
                ('mac', models.CharField(blank=True, max_length=128, verbose_name='mac地址')),
                ('mac_vendor', models.CharField(blank=True, max_length=128, verbose_name='厂家')),
                ('up', models.BooleanField(default=True, verbose_name='存活状态')),
                ('extra', models.TextField(default='', verbose_name='额外补充信息')),
                ('comment', models.TextField(default='-', verbose_name='系统部件描述')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '主机设备表',
                'db_table': 'hosts',
            },
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='协议')),
            ],
            options={
                'verbose_name': '协议组',
                'db_table': 'protocols',
            },
        ),
        migrations.CreateModel(
            name='ReportFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format_func', models.CharField(blank=True, max_length=155, verbose_name='格式化函数')),
            ],
            options={
                'verbose_name': '报告格式化',
                'db_table': 'report_formats',
            },
        ),
        migrations.CreateModel(
            name='ScanRecode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('target', models.GenericIPAddressField(verbose_name='扫描的IP目标')),
                ('port', models.IntegerField(verbose_name='扫描端口')),
                ('output', models.CharField(blank=True, max_length=255, verbose_name='保存路径')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '扫描事件',
                'db_table': 'scan_recode',
            },
        ),
        migrations.CreateModel(
            name='ScanReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('report', models.TextField(default='', verbose_name='格式化后的报告文本')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('scan_recode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scan_output_report', to='scan.ScanRecode')),
            ],
            options={
                'verbose_name': '扫描报告',
                'db_table': 'scan_reports',
            },
        ),
        migrations.CreateModel(
            name='ScanTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('targets', models.TextField(help_text='必须是IPv4格式', verbose_name='扫描的目标集群')),
                ('scan_interval', models.IntegerField(default=86400, help_text='*/2 * * * *', verbose_name='Crontab扫描')),
                ('scan_crontab', models.CharField(default='0 0 * * *', help_text='*/2 * * * *', max_length=55, verbose_name='Crontab扫描')),
            ],
            options={
                'verbose_name': '主机服务探测',
                'db_table': 'scan_tasks',
            },
        ),
        migrations.CreateModel(
            name='ScanTool',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=55, verbose_name='扫描器英文名称')),
                ('used_script', models.TextField(default='', verbose_name='使用命令')),
                ('_kwargs', models.TextField(default='', help_text='扫描参数-h', verbose_name='需要准备的参数集合')),
                ('extra', models.TextField(default='', verbose_name='额外补充信息')),
                ('comment', models.TextField(default='', verbose_name='扫描器设定描述')),
                ('protocol', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='scan_protocol', to='scan.Protocol', verbose_name='针对协议')),
            ],
            options={
                'verbose_name': '扫描工具集合',
                'db_table': 'scan_tools',
            },
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('scan_tools', models.ManyToManyField(blank=True, related_name='scan_tools_2_scheme', to='scan.ScanTool')),
            ],
            options={
                'verbose_name': '扫描方案',
                'db_table': 'scan_scheme',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('port', models.CharField(blank=True, max_length=7, verbose_name='端口')),
                ('hostname', models.CharField(blank=True, max_length=55, verbose_name='主机名')),
                ('banner', models.CharField(blank=True, max_length=155, verbose_name='产品')),
                ('protocol', models.CharField(blank=True, max_length=255, verbose_name='协议')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='状态')),
                ('service', models.CharField(blank=True, max_length=255, verbose_name='服务')),
                ('version', models.CharField(blank=True, max_length=255, verbose_name='版本')),
                ('reason', models.CharField(blank=True, max_length=255, verbose_name='反馈原因')),
                ('descover_time', models.DateTimeField(verbose_name='发现时间')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_service', to='scan.Host')),
            ],
            options={
                'verbose_name': '主机服务探测',
                'db_table': 'host_services',
            },
        ),
        migrations.CreateModel(
            name='Xprotocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(blank=True, max_length=255, verbose_name='归纳协议')),
                ('xprotocol', models.CharField(blank=True, max_length=255, verbose_name='模糊协议')),
            ],
            options={
                'verbose_name': '协议对照表',
                'db_table': 'xprotocols',
            },
        ),
        migrations.AddField(
            model_name='scantask',
            name='scan_scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_2_scheme', to='scan.Scheme', verbose_name=''),
        ),
        migrations.AddField(
            model_name='scanrecode',
            name='scan_tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scan_event_2_scan_tool', to='scan.ScanTool', verbose_name='使用的扫描工具'),
        ),
        migrations.AddField(
            model_name='reportformat',
            name='scan_tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scan_out_put_format', to='scan.ScanTool'),
        ),
    ]