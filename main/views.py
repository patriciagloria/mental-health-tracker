from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275172',
        'name': 'Patricia Gloria Sujatmoko Silaban',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)