# Imports
from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random

# Functions
# ----------

# convert function from .md to .html
# ----------------------------------


def converter(t):
    content = util.get_entry(t)
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

def enter(request, t):
    hcont = converter(t)
    if hcont != None:
        return render(request, "encyclopedia/enter.html", {
            "t": t,
            "content": hcont
        })
    else:
        return render(request, 'encyclopedia/error.html', {
                'message': '<span class="important">Sorry</span>, the entry <span class="important"><b>(</span> '+ t +' <span class="important">)</b></span> was not found <span class="important">!</span>'
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
        t = request.POST['t']
        tit_none = util.get_entry(t)
        if tit_none is not None:
            return render(request, 'encyclopedia/error.html', {
                'message': 'Indeed, there is a page in the name of <span class="important"><b>(</span> '+ t + ' <span class="important">)</span></b>',
            })
        else:
            util.save_entry(t, content)
            h_cont = converter(t)
            return render(request, "encyclopedia/enter.html", {
                'title': t,
                'content': h_cont
            })


# wiki edit page function
# -----------------------

def edit(request):
    if request.method == "POST":
        t = request.POST['entered_t']
        content = util.get_entry(t)
        return render(request, 'encyclopedia/edit.html', {
            'title': t,
            'content': content
        })


# save edit in memory function
# ----------------------------

def saveedit(request):
    if request.method == "POST":
        t = request.POST['t']
        content = request.POST['content']
        util.save_entry(t, content)
        h_cont = converter(t)
        return render(request, "encyclopedia/enter.html", {
            'title': t,
            'content': h_cont
        })
