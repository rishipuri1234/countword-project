from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    # print('hey',fulltext)
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1

        else:
            worddictionary[word] = 1
    wordsorted = sorted(worddictionary.items(), key= operator.itemgetter(1), reverse= True)
    return render(request,'count.html',{ 'length': len(wordlist), 'fulltext': fulltext, 'count': len(worddictionary), 'worddictionary': wordsorted})