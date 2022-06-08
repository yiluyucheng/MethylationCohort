from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

from jinja2 import Environment, FileSystemLoader
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Grid
from random import randrange
from collections import Counter
import json
from rest_framework.views import APIView
from pyecharts.globals import CurrentConfig
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./cohort/templates"))
 

def homeview(request, glist=None, searchs=None):
    # display table and seperate pages
    if glist is None:
        cohort_list = cohort.objects.all().order_by('-count')
    else:
        cohort_list = glist
    if cohort_list:
        paginator = Paginator(cohort_list, 5)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        return render(request, 'home.html',
                      {'page_obj': page_obj, 'paginator': paginator,
                       'is_paginated': True, })
    else:
        return render(request, 'home.html')
   
    
def density_count(d_list, bin=5):
    ## calculate counts in each interval
    d_list = [int(i // bin) for i in d_list]
    dkeys = [i for i in range(min(d_list + [0]), max(d_list + [19]) + 1)]
    d_all = dict(zip(dkeys, [0]*len(dkeys)))
    d_all.update(Counter(d_list))
    dx = [bin * i for i in list(d_all.keys())]
    dy = list(d_all.values())
    return dx, dy

   
   
###################################    
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error

    
def grid_base(group_list, integer_list) -> Grid:

    dx, dy = density_count(integer_list)
    bar = (    
        Bar()
        .add_xaxis(dx)
        .add_yaxis("", dy, category_gap=1, itemstyle_opts=opts.ItemStyleOpts(color='#f07167'))
        #.set_global_opts(title_opts=opts.TitleOpts(title="Grid-Bar"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )

    pie = (
        Pie()
        .add("", group_list, center=["25%", "50%"])
        .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .set_global_opts(
            #title_opts=opts.TitleOpts(title="Grid-Line", pos_top="10%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    
    c = (
        Grid()
        .add(bar, grid_opts=opts.GridOpts(pos_left="55%"))
        .add(pie, grid_opts=opts.GridOpts(pos_top="30%", pos_right="75%"))
        .dump_options_with_quotes()
    )
    return c 
    

class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        #gse = 'GSE55763'
        gse = request.GET['gse']
        s_list = GsmInfo.objects.filter(series__contains=gse)
        group_list = list(Counter(s_list.values_list('gender', flat=True)).items())
        integer_list = s_list.values_list('age', flat=True)
        return JsonResponse(json.loads(grid_base(group_list, integer_list)))


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        gse = request.GET['gse']
        #gse = 'GSE55763'
        glist = cohort.objects.filter(ids__contains=gse)[0]
        return render(request, 'index_bar.html', {'GSE': glist, })        
                