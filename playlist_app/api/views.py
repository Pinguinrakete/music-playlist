from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
from .serializer import PlaylistSerializer
from playlist_app.models import Playlist

@api_view(['GET','POST'])
def playlist_view(request):

    if request.method == 'GET':
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True, context={'request': request})
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['GET','DELETE','PUT'])
def playlist_single_view(request, pk):

    if request.method == 'GET':
        playlist = Playlist.objects.get(pk=pk)
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        playlist = Playlist.objects.get(pk=pk)
        serializer = PlaylistSerializer(playlist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        playlist = Playlist.objects.get(pk=pk)
        serializer = PlaylistSerializer(playlist)
        playlist.delete()
        return Response(serializer.data)