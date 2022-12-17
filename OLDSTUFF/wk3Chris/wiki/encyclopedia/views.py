from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    return(request, "encyclopedia/index.html"), {
        "entry": util.get_entry(title)
    }

