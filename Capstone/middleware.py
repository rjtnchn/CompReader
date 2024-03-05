from django.shortcuts import redirect
from django.urls import reverse

class ReadingTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/questions/'):
            # Check if the user has already read the poem for 10 minutes
            # If not, redirect them back to the poem view
            if not request.session.get('poem_read'):
                return redirect(reverse('poem', args=[request.session.get('poem_id')]))

        response = self.get_response(request)
        return response
