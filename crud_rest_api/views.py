from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from crud_rest_api.serializers import UserSerializer, GroupSerializer, WidgetsSerializer

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden

from crud_rest_api.models import Widgets
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpRequest


# Modular methods

@csrf_exempt
def get_widgets(request: HttpRequest):
    if request.method == 'GET':
        widgets = Widgets.objects.all()
        serializer = WidgetsSerializer(widgets, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponseForbidden('Method not allowed')


@csrf_exempt
def add_widgets(request: HttpRequest):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WidgetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponseForbidden('Method not allowed')


@csrf_exempt
def get_widget(request: HttpRequest, pk):
    if request.method == 'GET':
        try:
            widget = Widgets.objects.get(pk=pk)
            serializer = WidgetsSerializer(widget)
            return JsonResponse(serializer.data)

        except Widgets.DoesNotExist:
            return HttpResponse(status=404)

    else:
        return HttpResponseForbidden('Method not allowed')


@csrf_exempt
def update_widget(request: HttpRequest, pk):
    if request.method == 'PUT':
        try:
            widget = Widgets.objects.get(pk=pk)
            data = JSONParser().parse(request)
            serializer = WidgetsSerializer(widget, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        except Widgets.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponseForbidden('Method not allowed')


@csrf_exempt
def delete_widget(request: HttpRequest, pk):
    if request.method == 'DELETE':
        try:
            widget = Widgets.objects.get(pk=pk)
            widget.delete()
            return HttpResponse(status=204)

        except Widgets.DoesNotExist:
            return HttpResponse(status=404)

    else:
        return HttpResponseForbidden('Method not allowed')

