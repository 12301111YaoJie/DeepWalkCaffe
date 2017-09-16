# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from connectMySQL import connectAndtoFlow 
def hello(req):
	print "Here....."
	#execfile("/home/yao/django_test/deepwalk/deepwalk/connectMySQL.py")
	connectAndtoFlow()
	print "end"	
	return HttpResponse("Hello world ! ")


