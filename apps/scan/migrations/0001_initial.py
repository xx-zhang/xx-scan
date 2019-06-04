# Generated by Django 2.1.7 on 2019-06-04 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='系统部件名称')),
                ('domain', models.CharField(blank=True, max_length=128, verbose_name='域名')),
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
            name='NmapServiceName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255, unique=True, verbose_name='服务名')),
                ('active', models.BooleanField(default=True, verbose_name='激活.当前有工具的状态')),
            ],
            options={
                'verbose_name': '协议对照表',
                'db_table': 'nmap_service_names',
            },
        ),
        migrations.CreateModel(
            name='PortRange',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='端口范围描述')),
                ('ports', models.TextField(blank=True, verbose_name='端口范围')),
            ],
            options={
                'verbose_name': '端口集合',
                'db_table': 'port_range',
            },
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocol', models.CharField(db_index=True, max_length=55, unique=True, verbose_name='协议')),
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
                ('path', models.CharField(blank=True, max_length=255, verbose_name='PATH路径')),
                ('domain', models.CharField(blank=True, max_length=255, verbose_name='域名')),
                ('output', models.CharField(blank=True, max_length=255, verbose_name='保存路径')),
                ('task_id', models.CharField(blank=True, max_length=155, verbose_name='任务ID')),
                ('script', models.TextField(blank=True, verbose_name='完整的执行脚本[生成]')),
                ('active', models.BooleanField(default=True, verbose_name='记录是否被激活')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '扫描事件记录',
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
            name='ScanScript',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=55, verbose_name='扫描脚本对应名称')),
                ('bin_name', models.CharField(blank=True, max_length=55, verbose_name='扫描器bin')),
                ('args', models.CharField(blank=True, max_length=155, verbose_name='脚本填充参数')),
                ('used_script', models.TextField(default='', verbose_name='使用命令')),
                ('protocol', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='scanscript_protocol', to='scan.Protocol', verbose_name='针对协议')),
            ],
            options={
                'verbose_name': '扫描工具集合',
                'db_table': 'scan_scripts',
            },
        ),
        migrations.CreateModel(
            name='ScanTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('service', '服务'), ('domain', '域名')], default='service', max_length=20, verbose_name='发现类型')),
                ('domains', models.TextField(default='baidu.com', help_text='baidu.com,sina.com.cn', verbose_name='域名名称集合')),
                ('imports_active', models.BooleanField(default=False, verbose_name='开启文件导入方式')),
                ('imports', models.FileField(blank=True, upload_to='imports/', verbose_name='导入扫描XML')),
                ('targets', models.TextField(default='127.0.0.1', help_text='必须是IPv4格式', verbose_name='扫描的目标集群')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('atnow', models.BooleanField(blank=True, verbose_name='立即执行')),
                ('regular', models.DateTimeField(blank=True, verbose_name='定时执行')),
                ('interval', models.IntegerField(blank=True, help_text='3600* 2', verbose_name='定时扫描')),
                ('crontab', models.CharField(blank=True, help_text='*/2 * * * *', max_length=55, verbose_name='Crontab模式')),
                ('ports', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='task_scan_port_range', to='scan.PortRange', verbose_name='端口范围')),
            ],
            options={
                'verbose_name': '扫描任务',
                'db_table': 'scan_tasks',
            },
        ),
        migrations.CreateModel(
            name='ScanTool',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=55, verbose_name='扫描脚本对应名称')),
                ('desc', models.TextField(default='', verbose_name='扫描器描述')),
                ('in_system', models.BooleanField(default=False, verbose_name='系统中存在')),
                ('judge_script', models.TextField(default='', verbose_name='判断是否在程序中的脚本')),
                ('help_scripts', models.TextField(default='', verbose_name='推荐的命令说明')),
                ('install', models.TextField(default='', verbose_name='执行的脚本命令行')),
                ('summary', models.TextField(default='', verbose_name='工具概要')),
                ('protocol', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='scantool_protocol', to='scan.Protocol', verbose_name='针对协议')),
            ],
            options={
                'verbose_name': '扫描工具',
                'db_table': 'scan_tools',
            },
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='方案名称')),
                ('desc', models.TextField(blank=True, verbose_name='方案描述')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('scan_tools', models.ManyToManyField(blank=True, related_name='scan_tools_2_scheme', to='scan.ScanScript')),
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
                ('running', models.BooleanField(default=True, verbose_name='运行中')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_service', to='scan.Host')),
            ],
            options={
                'verbose_name': '主机服务探测',
                'db_table': 'host_services',
            },
        ),
        migrations.CreateModel(
            name='ServicePort',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('port', models.IntegerField(verbose_name='端口数值')),
                ('port_name', models.CharField(blank=True, max_length=255, verbose_name='端口名称')),
                ('desc', models.CharField(blank=True, max_length=255, verbose_name='端口描述')),
                ('type', models.CharField(blank=True, max_length=255, verbose_name='类型')),
                ('type_desc', models.CharField(blank=True, max_length=255, verbose_name='类型描述')),
                ('protocol', models.CharField(default='tcp', max_length=30, verbose_name='传输层协议')),
            ],
            options={
                'verbose_name': '常见服务端口映射表',
                'db_table': 'service_port',
            },
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='空间名称推荐英文', max_length=55, verbose_name='空间名称')),
                ('desc', models.TextField(blank=True, help_text='描述', verbose_name='描述')),
                ('summary', models.TextField(blank=True, verbose_name='空间简介')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_workspace', to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
            options={
                'verbose_name': '用户空间',
                'db_table': 'workspace',
            },
        ),
        migrations.AddField(
            model_name='scantask',
            name='scan_scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_2_scheme', to='scan.Scheme', verbose_name='扫描方案'),
        ),
        migrations.AddField(
            model_name='scantask',
            name='workspace',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='wk_task', to='scan.Workspace', verbose_name='工作组'),
        ),
        migrations.AddField(
            model_name='scanrecode',
            name='scan_tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scan_event_2_scan_tool', to='scan.ScanScript', verbose_name='使用的扫描工具'),
        ),
        migrations.AddField(
            model_name='scanrecode',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scan_service2code', to='scan.Service', verbose_name='需要扫描记录的服务'),
        ),
        migrations.AddField(
            model_name='reportformat',
            name='scan_tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scan_out_put_format', to='scan.ScanScript'),
        ),
        migrations.AddField(
            model_name='nmapservicename',
            name='protocol',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='nmap_service_protocol', to='scan.Protocol', verbose_name='针对协议'),
        ),
        migrations.AddField(
            model_name='host',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspace_hosts', to='scan.Workspace'),
        ),
    ]
