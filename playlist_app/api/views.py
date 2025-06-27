from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
from .serializer import PlaylistSerializer
from playlist_app.models import Playlist

@api_view(['GET','POST'])
def playlist_view(request):

    if request.method == 'GET':
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(markets, many=True, context={'request': request})
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PlalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)