from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db import models

def get_model(label):
    try:
        Model = models.get_model(*label.split("."))
    except TypeError:
        path, model = label.rsplit(".", 1)
        module = __import__(path, globals(), locals(), [model])
        Model = getattr(module, model)
    return Model

def djdash(request):
    _models = []
    for model in models.get_models():
        _models.append([model.__name__, "%s.%s" % (model.__module__, model.__name__)])

    context = {
        "models": _models,
    }
    return render_to_response("djdash/index.html", RequestContext(request, context))