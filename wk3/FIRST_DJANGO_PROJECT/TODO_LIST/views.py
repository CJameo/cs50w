from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

tasks = ["foo", "bar", "baz"]

class NewTODOForm(forms.Form):
    task = forms.CharField(label="New TODO")

# Create your views here.
def index(request):

    # Check if there already exists a "tasks" key in our session

    if "tasks" not in request.session:

        # If not, create a new list
        request.session["tasks"] = []

    return render(request, "TODO_LIST/index.html", {
        "tasks": request.session["tasks"]
    })

# Add a new task:
def add(request):
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewTODOForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            # Add the new task to our list of tasks
            request.session["tasks"] += [task]

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("TODO_LIST:index"))
        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "TODO_LIST/add.html", {
                "form": form
            })

    return render(request, "TODO_LIST/add.html", {
        "form": NewTODOForm()
    })