# from django.shortcuts import redirect
# from django.urls import reverse

# class ReadingTimeMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.path.startswith('/questions/'):
#             # Check if the user has already read the poem for 10 minutes
#             # If not, redirect them back to the poem view
#             if not request.session.get('poem_read'):
#                 # Redirect to the poem view with the appropriate poem_id
#                 poem_id = request.session.get('poem_id')
#                 return redirect(reverse('display_poem', kwargs={'difficulty_id': poem_id}))

#         response = self.get_response(request)
#         return response
