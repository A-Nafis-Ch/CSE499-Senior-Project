# context_processors.py

def user_context(request):
    context = {}
    if request.user.is_authenticated:
        context['user_name'] = request.user.username
    return context
