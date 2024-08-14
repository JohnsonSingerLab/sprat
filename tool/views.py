# tool/views.py
from django.shortcuts import render

def grapetree_view(request):
    return render(request, 'grapetree.html')

def index_view(request):
    return render(request, 'index.html')



# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, World!")
    


# from datetime import datetime

# from django.http import HttpResponse

# def index(request):
#     now = datetime.now()
#     html = f'''
#     <html>
#         <body>
#             <h1>Hello from Vercel!</h1>
#             <p>The current time is { now }.</p>
#         </body>
#     </html>
#     '''
#     return HttpResponse(html)