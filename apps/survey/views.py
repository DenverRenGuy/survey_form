from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    request.session.setdefault('attempt', 0)
    request.session.setdefault('name', '')
    request.session.setdefault('dojo', '')
    request.session.setdefault('language', '')
    request.session.setdefault('comment', '')

    return render(request, 'survey/index.html')

def result(request):

    return redirect(request, '/')

def process(request):

    rs = request.session
    rp = request.POST
    if request.method == 'POST':
        rs['attempt'] += 1
        rs['name'] = rp['name']
        rs['dojo'] = rp['dojo']
        rs['language'] = rp['language']
        rs['comment'] = rp['comment']
        return render(request, 'survey/result.html')

    else:

        return render(request, 'survey/result.html')
