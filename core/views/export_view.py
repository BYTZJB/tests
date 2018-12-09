#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by YangWei on 2018/7/17
from django.http import HttpResponse
from django.views import View

from core.admin import BookResource


class ExportView(View):

    def get(self, request):
        data_set = BookResource().export()
        # xls格式
        response = HttpResponse(data_set.xls,
                                content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="persons.xls"'
        return response




if __name__ == '__main__':
    pass
