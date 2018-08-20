# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CustomerCare(models.Model):
    care_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('CustomerInfo', models.DO_NOTHING, blank=True, null=True)
    care_theme = models.CharField(max_length=50, blank=True, null=True)
    care_way = models.CharField(max_length=50, blank=True, null=True)
    care_time = models.DateTimeField()
    care_remark = models.CharField(max_length=1000, blank=True, null=True)
    care_nexttime = models.DateTimeField()
    care_people = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'customer_care'


class CustomerCondition(models.Model):
    condition_id = models.AutoField(primary_key=True)
    condition_name = models.CharField(max_length=50, blank=True, null=True)
    condition_explain = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'customer_condition'


class CustomerInfo(models.Model):
    customer_id = models.AutoField(primary_key=True)
    condition = models.ForeignKey(CustomerCondition, models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('CustomerSource', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('CustomerType', models.DO_NOTHING, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_sex = models.CharField(max_length=10, blank=True, null=True)
    customer_mobile = models.CharField(max_length=20, blank=True, null=True)
    customer_qq = models.CharField(max_length=20, blank=True, null=True)
    customer_address = models.CharField(max_length=500, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_remark = models.CharField(max_length=1000, blank=True, null=True)
    customer_job = models.CharField(max_length=100, blank=True, null=True)
    customer_blog = models.CharField(max_length=100, blank=True, null=True)
    customer_tel = models.CharField(max_length=20, blank=True, null=True)
    customer_msn = models.CharField(max_length=50, blank=True, null=True)
    birth_day = models.DateTimeField()
    customer_addtime = models.DateTimeField()
    customer_addman = models.CharField(max_length=50, blank=True, null=True)
    customer_changtime = models.DateTimeField()
    change_man = models.CharField(max_length=20, blank=True, null=True)
    customer_company = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'customer_info'


class CustomerLinkman(models.Model):
    linkman_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    linkman_name = models.CharField(max_length=50, blank=True, null=True)
    linkman_sex = models.CharField(max_length=20, blank=True, null=True)
    linkman_job = models.CharField(max_length=100, blank=True, null=True)
    linkman_mobile = models.CharField(max_length=20, blank=True, null=True)
    linkman_age = models.IntegerField(blank=True, null=True)
    linkman_relation = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'customer_linkman'


class CustomerLinkreord(models.Model):
    record_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    link_time = models.DateTimeField()
    who_link = models.CharField(max_length=50, blank=True, null=True)
    link_type = models.CharField(max_length=50, blank=True, null=True)
    link_theme = models.CharField(max_length=200, blank=True, null=True)
    link_nexttime = models.DateTimeField()
    link_remark = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'customer_linkreord'


class CustomerSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'customer_source'


class CustomerType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'customer_type'


class DepartmentInfo(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50, blank=True, null=True)
    department_desc = models.CharField(max_length=500, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'department_info'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'


class EmailInfo(models.Model):
    email_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    email_content = models.CharField(max_length=2000, blank=True, null=True)
    email_time = models.DateTimeField()
    email_state = models.CharField(max_length=50, blank=True, null=True)
    email_theme = models.CharField(max_length=200, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'email_info'


class HouseInfo(models.Model):
    house_id = models.AutoField(primary_key=True)
    type = models.ForeignKey('HouseType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    house_address = models.CharField(max_length=500, blank=True, null=True)
    house_price = models.IntegerField(blank=True, null=True)
    house_ambient = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'house_info'


class HouseType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'house_type'


class NoticeInfo(models.Model):
    notice_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    notice_item = models.CharField(max_length=100, blank=True, null=True)
    notice_content = models.CharField(max_length=2000, blank=True, null=True)
    notice_time = models.DateTimeField()
    notice_endtime = models.DateTimeField()
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'notice_info'


class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(DepartmentInfo, models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('UserRole', models.DO_NOTHING, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_sex = models.CharField(max_length=10, blank=True, null=True)
    user_mobile = models.CharField(max_length=20, blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)
    user_address = models.CharField(max_length=500, blank=True, null=True)
    user_num = models.CharField(max_length=100, blank=True, null=True)
    user_pw = models.CharField(max_length=50, blank=True, null=True)
    user_tel = models.CharField(max_length=20, blank=True, null=True)
    user_idnum = models.CharField(max_length=20, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_addtime = models.DateTimeField()
    user_addman = models.CharField(max_length=50, blank=True, null=True)
    user_changetime = models.DateTimeField()
    user_changeman = models.CharField(max_length=50, blank=True, null=True)
    user_intest = models.CharField(max_length=1000, blank=True, null=True)
    user_diploma = models.CharField(max_length=20, blank=True, null=True)
    user_bankcard = models.CharField(max_length=20, blank=True, null=True)
    user_nation = models.CharField(max_length=20, blank=True, null=True)
    is_married = models.CharField(max_length=10, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'user_info'


class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, blank=True, null=True)
    role_power = models.IntegerField(blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        
        db_table = 'user_role'
