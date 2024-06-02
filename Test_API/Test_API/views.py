# TEST_API/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
@api_view(['GET'])
def hello_world(request):
    """
    Returns a simple 'TEST' message.
    """
    return Response({'message': 'Hey Farouk'})

@api_view(['POST'])
def upload_resume(request):
    """
    Upload a resume file.
    """
    if 'resume' in request.FILES:
        resume_file = request.FILES['resume']
        # Process the uploaded file (e.g., save it, analyze it, etc.)
        # You can access the file name using: resume_file.name
        return Response({'success': True})
    else:
        return Response({'success': False, 'message': 'No resume file provided.'})