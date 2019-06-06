import xadmin


from ...models import ScanScript, ScanRecode, ScanTool, Scheme

class ScanScriptAdmin(object):
    list_display = ('name', "bin_name", "args", 'protocol', 'used_script')

xadmin.site.register(ScanScript, ScanScriptAdmin)


class ScanToolAdmin(object):
    list_display = ("name", "in_system", "protocol", "summary")

    fieldsets = [
        ("介绍", {'fields': ['name', "desc", "summary","help_scripts"]}),
        ('安装', {'fields': ['in_system', 'install']}),
        ('检查', {'fields': ['judge_script'], 'classes': ['collapse']}),
    ]

xadmin.site.register(ScanTool, ScanToolAdmin)


## 扫描 Recode 记录管理
class ScanRecodeAdmin(object):

    def queryset(self):
        from website.settings import PREVILEGED_USER_SETS
        qs = super(ScanRecodeAdmin, self).queryset()
        if self.request.user.username in PREVILEGED_USER_SETS:
            return qs
        else:
            return qs.filter(service__host__workspace__user=self.request.user)

    list_display = ("service", "scan_tool", "active", "domain")

    #readonly_fields = ('create_user', )


xadmin.site.register(ScanRecode, ScanRecodeAdmin)




