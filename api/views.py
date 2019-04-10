from rest_framework.decorators import api_view
from rest_framework.response import Response

from utility.firebase import db


@api_view(['GET'])
def get_document(request):

    data = db.collection('completedEntries').document('wNiBpVjuMSVUf0KEwd8x').get()
    return Response(data.to_dict())