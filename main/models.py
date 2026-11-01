#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    xuexiao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学校' )
    xueli=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学历' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    nianling=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    '''
    yonghuzhanghao=VARCHAR
    mima=VARCHAR
    yonghuxingming=VARCHAR
    xingbie=VARCHAR
    lianxifangshi=VARCHAR
    touxiang=Text
    xuexiao=VARCHAR
    xueli=VARCHAR
    youxiang=VARCHAR
    nianling=Integer
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class qiye(BaseModel):
    __doc__ = u'''qiye'''
    __tablename__ = 'qiye'

    __loginUser__='qiyezhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='qiyezhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qiyezhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='企业账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    qiyemingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='企业名称' )
    farenxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='法人姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    yingyezhizhao=models.TextField   (  null=True, unique=False, verbose_name='营业执照' )
    qiyeyouxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业邮箱' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    qiyezhanghao=VARCHAR
    mima=VARCHAR
    qiyemingcheng=VARCHAR
    farenxingming=VARCHAR
    lianxidianhua=VARCHAR
    yingyezhizhao=Text
    qiyeyouxiang=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'qiye'
        verbose_name = verbose_name_plural = '企业'
class zhiweifenlei(BaseModel):
    __doc__ = u'''zhiweifenlei'''
    __tablename__ = 'zhiweifenlei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhiweifenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位分类' )
    '''
    zhiweifenlei=VARCHAR
    '''
    class Meta:
        db_table = 'zhiweifenlei'
        verbose_name = verbose_name_plural = '职位分类'
class qiyexinxi(BaseModel):
    __doc__ = u'''qiyexinxi'''
    __tablename__ = 'qiyexinxi'



    __authTables__={'qiyezhanghao':'qiye',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业名称' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    qiyeyouxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业邮箱' )
    qiyeleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业类型' )
    qiyefengmian=models.TextField   (  null=True, unique=False, verbose_name='企业封面' )
    qiyexingzhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业性质' )
    yuangongrenshu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='员工人数' )
    qiyejieshao=models.TextField   (  null=True, unique=False, verbose_name='企业介绍' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    '''
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    lianxidianhua=VARCHAR
    qiyeyouxiang=VARCHAR
    qiyeleixing=VARCHAR
    qiyefengmian=Text
    qiyexingzhi=VARCHAR
    yuangongrenshu=VARCHAR
    qiyejieshao=Text
    clicktime=DateTime
    clicknum=Integer
    '''
    class Meta:
        db_table = 'qiyexinxi'
        verbose_name = verbose_name_plural = '企业信息'
class zhaopinxinxi(BaseModel):
    __doc__ = u'''zhaopinxinxi'''
    __tablename__ = 'zhaopinxinxi'



    __authTables__={'qiyezhanghao':'qiye',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhiweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位名称' )
    zhiweifenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位分类' )
    zhiweifengmian=models.TextField   (  null=True, unique=False, verbose_name='职位封面' )
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业名称' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    xinzidaiyu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='薪资待遇' )
    gongzuodidian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工作地点' )
    gongzuoshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工作时间' )
    faburiqi=models.DateField   (  null=True, unique=False, verbose_name='发布日期' )
    gongzuoneirong=models.TextField   (  null=True, unique=False, verbose_name='工作内容' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    '''
    zhiweimingcheng=VARCHAR
    zhiweifenlei=VARCHAR
    zhiweifengmian=Text
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    lianxidianhua=VARCHAR
    xinzidaiyu=VARCHAR
    gongzuodidian=VARCHAR
    gongzuoshijian=VARCHAR
    faburiqi=Date
    gongzuoneirong=Text
    clicktime=DateTime
    clicknum=Integer
    '''
    class Meta:
        db_table = 'zhaopinxinxi'
        verbose_name = verbose_name_plural = '招聘信息'
class yingpinxinxi(BaseModel):
    __doc__ = u'''yingpinxinxi'''
    __tablename__ = 'yingpinxinxi'



    __authTables__={'qiyezhanghao':'qiye','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhiweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位名称' )
    zhiweifenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位分类' )
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业名称' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    xinzidaiyu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='薪资待遇' )
    gongzuodidian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工作地点' )
    gongzuoshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工作时间' )
    yingpinshijian=models.DateField   (  null=True, unique=False, verbose_name='应聘时间' )
    gerenjianli=models.TextField   (  null=True, unique=False, verbose_name='个人简历' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    xueli=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学历' )
    xuexiao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学校' )
    '''
    zhiweimingcheng=VARCHAR
    zhiweifenlei=VARCHAR
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    lianxidianhua=VARCHAR
    xinzidaiyu=VARCHAR
    gongzuodidian=VARCHAR
    gongzuoshijian=VARCHAR
    yingpinshijian=Date
    gerenjianli=Text
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    lianxifangshi=VARCHAR
    xueli=VARCHAR
    xuexiao=VARCHAR
    '''
    class Meta:
        db_table = 'yingpinxinxi'
        verbose_name = verbose_name_plural = '应聘信息'
class mianshitongzhi(BaseModel):
    __doc__ = u'''mianshitongzhi'''
    __tablename__ = 'mianshitongzhi'



    __authTables__={'qiyezhanghao':'qiye','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhiweimingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='职位名称' )
    zhiweifenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位分类' )
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业名称' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    xinzidaiyu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='薪资待遇' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    xueli=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学历' )
    xuexiao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学校' )
    mianshishijian=models.DateField   (  null=True, unique=False, verbose_name='面试时间' )
    mianshitongzhi=models.TextField   (  null=True, unique=False, verbose_name='面试通知' )
    '''
    zhiweimingcheng=VARCHAR
    zhiweifenlei=VARCHAR
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    lianxidianhua=VARCHAR
    xinzidaiyu=VARCHAR
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    lianxifangshi=VARCHAR
    xueli=VARCHAR
    xuexiao=VARCHAR
    mianshishijian=Date
    mianshitongzhi=Text
    '''
    class Meta:
        db_table = 'mianshitongzhi'
        verbose_name = verbose_name_plural = '面试通知'
class mianshijieguo(BaseModel):
    __doc__ = u'''mianshijieguo'''
    __tablename__ = 'mianshijieguo'



    __authTables__={'qiyezhanghao':'qiye','yonghuzhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhiweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位名称' )
    zhiweifenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职位分类' )
    qiyezhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业账号' )
    qiyemingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='企业名称' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    xinzidaiyu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='薪资待遇' )
    yonghuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户账号' )
    yonghuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户姓名' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    xueli=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学历' )
    xuexiao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学校' )
    mianshijieguo=models.CharField ( max_length=255, null=True, unique=False, verbose_name='面试结果' )
    jiuyeshijian=models.DateField   (  null=True, unique=False, verbose_name='就业时间' )
    beizhu=models.TextField   (  null=True, unique=False, verbose_name='备注' )
    '''
    zhiweimingcheng=VARCHAR
    zhiweifenlei=VARCHAR
    qiyezhanghao=VARCHAR
    qiyemingcheng=VARCHAR
    lianxidianhua=VARCHAR
    xinzidaiyu=VARCHAR
    yonghuzhanghao=VARCHAR
    yonghuxingming=VARCHAR
    lianxifangshi=VARCHAR
    xueli=VARCHAR
    xuexiao=VARCHAR
    mianshijieguo=VARCHAR
    jiuyeshijian=Date
    beizhu=Text
    '''
    class Meta:
        db_table = 'mianshijieguo'
        verbose_name = verbose_name_plural = '面试结果'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型(1:收藏,21:赞,22:踩,31:竞拍参与,41:关注)' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告信息'
