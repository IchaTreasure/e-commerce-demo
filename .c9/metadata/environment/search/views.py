{"filter":false,"title":"views.py","tooltip":"/search/views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":25},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":6,"column":67},"action":"insert","lines":["from django.shortcuts import render","from products.models import Product","","# Create your views here.","def do_search(request):","    products = Product.objects.filter(name__icontains=request.GET['q'])","    return render(request, \"products.html\", {\"products\": products})"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":67},"end":{"row":6,"column":67},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590757994493,"hash":"97153b7f3f1b7e6bbacd0f793b00c533de75c2f1"}