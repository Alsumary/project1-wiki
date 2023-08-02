# Imports
from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random

# Functions
# ----------

# convert function from .md to .html
# ----------------------------------


def converter(title):
    content = util.get_entry(title)
    pr_markdown = Markdown()
    if content != None:
        return pr_markdown.convert(content)
    else:
        return None


# first page function
# -------------------

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# enter wiki page function
# ------------------------

def enter(request, title):
    hcont = converter(title)
    if hcont != None:
        return render(request, "encyclopedia/enter.html", {
            "title": title,
            "content": hcont
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "This Entry doesn't exist"
        })


# random wiki page function
# -------------------------

def random_page(request):
    entires = util.list_entries()
    random_entry = random.choice(entires)
    h_cont = converter(random_entry)
    return render(request, 'encyclopedia/enter.html', {
        'content': h_cont,
        'title': random_entry
    })


# search wiki page function
# -------------------------

def search(request):
    if request.method == "POST":
        s_enter = request.POST['q']
        enter_ex = converter(s_enter)
        if enter_ex != None:
            return render(request, "encyclopedia/enter.html", {
                'title': s_enter,
                'content': enter_ex
            })
        else:
            recom = []
            entiers = util.list_entries()
            for i in entiers:
                if s_enter.lower() in i.lower():
                    recom.append(i)
            return render(request, "encyclopedia/search.html", {
                'recom': recom
            })


# New page function
# -----------------

def pagenew(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        content = request.POST['content']
        title = request.POST['title']
        tit_none = util.get_entry(title)
        if tit_none is not None:
            return render(request, 'encyclopedia/error.html', {
                'message': 'Entry page already exists'
            })
        else:
            util.save_entry(title, content)
            h_cont = converter(title)
            return render(request, "encyclopedia/enter.html", {
                'title': title,
                'content': h_cont
            })


# wiki edit page function
# -----------------------

def edit(request):
    if request.method == "POST":
        title = request.POST['entered_title']
        content = util.get_entry(title)
        return render(request, 'encyclopedia/edit.html', {
            'title': title,
            'content': content
        })


# save edit in memory function
# ----------------------------

def saveedit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        h_cont = converter(title)
        return render(request, "encyclopedia/enter.html", {
            'title': title,
            'content': h_cont
        })
