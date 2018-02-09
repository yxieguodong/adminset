#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from appconf.models import Project
# Create your models here.
DEPLOY_POLICY = (
    ("Direct", "Direct"),
    # ("BlueGreen", "BlueGreen"),
)


class Delivery(models.Model):
    job_name = models.ForeignKey(Project, null=False, verbose_name=u"项目名", unique=True)
    deploy_num = models.IntegerField(verbose_name=u"当前部署次数", default=0)
    description = models.CharField(max_length=255, verbose_name=u"描述", null=True, blank=True)
    deploy_policy = models.CharField(max_length=255, choices=DEPLOY_POLICY, verbose_name=u"部署策略")
    build_clean = models.BooleanField(verbose_name=u"清理构建", default=False)
    shell = models.CharField(max_length=255, verbose_name=u"shell", blank=True)
    shell_position = models.BooleanField(verbose_name=u"本地执行", default=False)
    status = models.BooleanField(verbose_name=u"部署状态", default=False)
    bar_data = models.IntegerField(default=0)

    def __unicode__(self):
        return self.job_name
