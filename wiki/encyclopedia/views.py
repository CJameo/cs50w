import re
from random import randint
from pprint import pprint

from django.shortcuts import render, redirect
from markdown2 import Markdown

from . import util
from .forms import PageForm, SubmitForm

markdowner = Markdown()

def index(request):
    print(util.list_entries())
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry:
        if request.method == "GET": # USE A FORM TO ELIMINATE "POST"
            pprint(request.GET)
            if request.GET.get('edit'):
                return render(request, "encyclopedia/entry.html", {
                    "title": title, 
                    "entry": entry,
                    "edit": True
                })
            else:
                return render(request, "encyclopedia/entry.html", {
                    "title": title,
                    "entry": markdowner.convert(entry)
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
    
def update(request):
    if request.method == "POST":
        context = {}
        form = PageForm(request.POST or None)
        context['form'] = form
        if form.is_valid():
            title=form.cleaned_data.get("title")
            body=form.cleaned_data.get("body")
            util.save_entry(title, body)
            request.method = "GET"
            return entry(request, title)
        else:
            return render(request, "encyclopedia/create_new_page.html")  
    elif request.method == "GET":
        return render(request, "encyclopedia/create_new_page.html") 

def random(request):
    entries =util.list_entries()
    title=entries[randint(0, len(entries)-1)]
    return entry(request, title)

