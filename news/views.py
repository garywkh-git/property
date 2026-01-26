


from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import News
from .models import Salesperson



def news_list(request):
    # Get all news, newest first
    all_news = News.objects.all().order_by('-created_at')
    
    # 4 news per page (2×2 grid)
    paginator = Paginator(all_news, 2)
    
    page = request.GET.get('page')
    news = paginator.get_page(page)
    
    return render(request, 'news/list.html', {'news': news})