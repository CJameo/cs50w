import re

from django.shortcuts import render, redirect

from . import util
from .forms import NewPageForm


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
    
def newpage(request):
    context = {}
    form = NewPageForm(request.POST or None)
    context['form'] = form
    if request.method == "POST":
        if form.is_valid():
            title=form.changed_data.get("title")
            body=form.changed_data.get("body")
            util.save_entry(title, body)
            return entry(request, title)
        else:
            return render(request, "encyclopedia/create_new_page.html")  
    elif request.method == "GET":
        return render(request, "encyclopedia/create_new_page.html")  