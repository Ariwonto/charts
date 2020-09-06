from django.shortcuts import render

# it is a default view.
# please go to the samples folder for others view

def catalogue(request):
 	return  render(request, 'catalogue.html')

def panel(request):
 	return  render(request, 'panel-1.html')

def panel2(request):
 	return  render(request, 'panel-2.html')

def panel3(request):
 	return  render(request, 'panel-3.html')

def panel4(request):
 	return  render(request, 'panel-4.html')

def panel5(request):
 	return  render(request, 'panel-5.html')

def test(request):
 	return  render(request, 'test.html')