import re
from logging import exception
from unittest import result
from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

def entry(request, title):
    entry = util.get_entry(title=title)
    if entry:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": util.get_entry(title=title),
            })
    return render(request, "encyclopedia/error.html", {"title": title,})

def search(request):
    query = request.GET['query']

    print(util.list_entries())
    if query in util.list_entries():
        return redirect('entry', title=query)
    else:
        results = []
        for entry in util.list_entries():
            if re.findall(query, entry, re.IGNORECASE):
                results.append(entry)
        return render(request, 'encyclopedia/search_results.html', {'search_results': results})

def new_page(request):
    pass
