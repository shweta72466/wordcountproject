from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return HttpResponse("Hello")
#    return HttpResponse('<h1>Eggs <h1\>')
    return render(request,'home.html')
    #return render(request,'home.html',{'TEXT':'this is me'})

def count(request):
    fulltext =request.GET['fulltext']
    #print(fulltext)
    wordlist=fulltext.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word]=1

    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')
