# from django.shortcuts import render, get_object_or_404
# from .models import Job

# def career_list(request):
#     jobs = Job.objects.filter(published=True).order_by('-posted_date')
#     return render(request, "careers/career_list.html", {"jobs": jobs})

# def career_detail(request, job_id):
#     job = get_object_or_404(Job, id=job_id, published=True)
#     return render(request, "careers/career_detail.html", {"job": job})

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Job

def career_list(request):
    # Get all published jobs
    jobs = Job.objects.filter(published=True).order_by('-posted_date')

    # Create paginator: 5 jobs per page
    paginator = Paginator(jobs, 6)

    # Get current page number from query string (?page=2)
    page_number = request.GET.get('page')

    # Get the page object
    page_obj = paginator.get_page(page_number)

    return render(request, "careers/career_list.html", {"listings": page_obj})

def career_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id, published=True)
    return render(request, "careers/career_detail.html", {"job": job})
