#i have created this file-Jatin
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    with open('/home/jatin/python/python_made_projects/django_practice/mysite/mysite/1.txt', 'r')as file:
        data = file.read()
    params = {'name':'jatin', 'place':'mars'}
    return render(request, 'index.html', params)

def about(request):
    return HttpResponse("""
    about <a href="/a">about</a>
                        <a href="remove"> removepunc</a>""")
def removepunc(request):
    #get text
    text = request.POST.get('text', 'default')


    #checkbox vlaue
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    punctuation_marks = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    #check which checkbox is on
    if removepunc=='on':
        analyzed = ""
        for char in text:
            if char not in punctuation_marks:
                analyzed+= char

        params = {'purpose':'Removed Punctuation', 'analyzed_data': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=='on':
        analyzed = ""
        for char in text:
            analyzed+= char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_data': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover=='on':
        analyzed = ""
        for char in text:
            if char!='\n' and char!='\r':
                analyzed += char

        params = {'purpose': 'New line removed', 'analyzed_data': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremover=='on':
        analyzed = ""
        for index, char in enumerate(text):
            if not (text[index]==' ' and text[index+1]==" "):
                analyzed += char
        params = {'purpose': 'New line removed', 'analyzed_data': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)

    if charcounter=='on':
        len_of_text = len(text)
        analyzed=f'The given data has {len_of_text} no. of character'
        params = {'purpose': 'Extra space removed', 'analyzed_data': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)
    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)