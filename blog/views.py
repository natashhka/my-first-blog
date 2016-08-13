from django.shortcuts import render

# Create your views here.ghg
def post_list(request):
    return render(request, 'blog/post_list.html', {})
