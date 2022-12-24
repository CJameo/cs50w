import re

from django.shortcuts import render, redirect

from . import util


def index(request):
    print(util.list_entries())
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "error_code": 404,
            "error_msg": "Requested Entry Not Found"
        })

def search(request):
    term = request.GET["term"]

    if term in util.list_entries():
        return redirect("encyclopedia:entry", title=term)
    else:
        results = []
        for entry in util.list_entries():
            if re.match(f".*{term.lower()}.*", entry.lower()):
                results.append(entry)
        
        return render(request, "encyclopedia/search_results.html", {"search_results": results})