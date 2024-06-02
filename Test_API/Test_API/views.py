# TEST_API/views.py
import os
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.conf import settings
@api_view(['GET'])
def hello_world(request):
    """
    Returns a simple 'TEST' message.
    """
    return Response({'message': 'Hey Farouk'})

# @api_view(['POST'])
# def upload_resume(request):
#     """
#     Upload a resume file.
#     """
#     if 'resume' in request.FILES:
#         resume_file = request.FILES['resume']
#         # Process the uploaded file (e.g., save it, analyze it, etc.)
#         # You can access the file name using: resume_file.name
#         return Response({'success': True})
#     else:
#         return Response({'success': False, 'message': 'No resume file provided.'})

class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(operation_description='Upload file...',)
    #@action(detail=False, methods=['post'])
    def post(self, request, format=None):
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            target_directory = 'uploads/'
            os.makedirs(os.path.join(settings.MEDIA_ROOT, target_directory), exist_ok=True)
            full_filename = os.path.join(settings.MEDIA_ROOT, target_directory, uploaded_file.name)
            # Process the uploaded file (e.g., save it, analyze it, etc.)
            with open(full_filename, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return Response({'message': 'File uploaded & saved successfully!'})
        else:
            return Response({'message': 'No file provided.'}, status=status.HTTP_400_BAD_REQUEST)