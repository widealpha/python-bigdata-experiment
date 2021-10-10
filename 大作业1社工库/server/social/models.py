# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BmList(models.Model):
    # id = models.CharField(max_length=25, blank=True, null=True)
    tpid = models.CharField(max_length=25, blank=True, null=True)
    id_number = models.CharField(max_length=25, blank=True, null=True)
    qq = models.CharField(max_length=25, blank=True, null=True)
    sh = models.CharField(max_length=25, blank=True, null=True)
    hip = models.CharField(max_length=25, blank=True, null=True)
    age = models.CharField(max_length=25, blank=True, null=True)
    bust = models.CharField(max_length=25, blank=True, null=True)
    weibo = models.CharField(max_length=250, blank=True, null=True)
    hobby = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    astro = models.CharField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    prize = models.CharField(max_length=1000, blank=True, null=True)
    weight = models.CharField(max_length=25, blank=True, null=True)
    height = models.CharField(max_length=25, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    nation = models.CharField(max_length=25, blank=True, null=True)
    bmdate = models.CharField(max_length=25, blank=True, null=True)
    tptotal = models.CharField(max_length=25, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    sequence = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=25, blank=True, null=True)
    appraise = models.CharField(max_length=1000, blank=True, null=True)
    waistline = models.CharField(max_length=25, blank=True, null=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)
    real_name = models.CharField(max_length=50, blank=True, null=True)
    birthplace = models.CharField(max_length=25, blank=True, null=True)
    pic_path_1 = models.CharField(max_length=100, blank=True, null=True)
    pic_path_3 = models.CharField(max_length=100, blank=True, null=True)
    pic_path_2 = models.CharField(max_length=100, blank=True, null=True)
    pic_path_5 = models.CharField(max_length=100, blank=True, null=True)
    pic_path_4 = models.CharField(max_length=100, blank=True, null=True)
    declaration = models.CharField(max_length=500, blank=True, null=True)
    support_team = models.CharField(max_length=50, blank=True, null=True)

    def to_json(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    class Meta:
        managed = False
        db_table = 'bm_list'


class RhsUsers(models.Model):
    use_id = models.IntegerField(blank=True, null=True)
    use_id_number = models.CharField(max_length=25, blank=True, null=True)
    use_qq = models.CharField(max_length=25, blank=True, null=True)
    use_hip = models.IntegerField(blank=True, null=True)
    use_tel = models.CharField(max_length=25, blank=True, null=True)
    use_img = models.CharField(max_length=50, blank=True, null=True)
    use_age = models.CharField(max_length=25, blank=True, null=True)
    use_sex = models.IntegerField(blank=True, null=True)
    use_imgs = models.CharField(max_length=250, blank=True, null=True)
    use_poll = models.IntegerField(blank=True, null=True)
    use_show = models.IntegerField(blank=True, null=True)
    use_bust = models.IntegerField(blank=True, null=True)
    use_weibo = models.CharField(max_length=50, blank=True, null=True)
    use_phone = models.CharField(max_length=50, blank=True, null=True)
    use_prize = models.CharField(max_length=25, blank=True, null=True)
    use_email = models.CharField(max_length=100, blank=True, null=True)
    use_astro = models.CharField(max_length=25, blank=True, null=True)
    use_nation = models.CharField(max_length=50, blank=True, null=True)
    use_weight = models.IntegerField(blank=True, null=True)
    use_answer = models.CharField(max_length=25, blank=True, null=True)
    use_school = models.CharField(max_length=100, blank=True, null=True)
    use_height = models.IntegerField(blank=True, null=True)
    use_address = models.CharField(max_length=250, blank=True, null=True)
    use_appraise = models.CharField(max_length=200, blank=True, null=True)
    use_reg_time = models.IntegerField(blank=True, null=True)
    use_zip_code = models.IntegerField(blank=True, null=True)
    use_username = models.CharField(max_length=50, blank=True, null=True)
    use_birthday = models.IntegerField(blank=True, null=True)
    use_specialty = models.CharField(max_length=25, blank=True, null=True)
    use_real_name = models.CharField(max_length=50, blank=True, null=True)
    use_waistline = models.CharField(max_length=25, blank=True, null=True)
    use_last_login = models.IntegerField(blank=True, null=True)
    use_prev_login = models.IntegerField(blank=True, null=True)
    use_birthplace = models.CharField(max_length=25, blank=True, null=True)

    def to_json(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

    class Meta:
        managed = False
        db_table = 'rhs_users'
