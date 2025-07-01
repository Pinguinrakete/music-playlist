from .permission import allCanGETButStaffOrAuthenticatedOnlyPOST
from playlist_app.models import Playlist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializer import PlaylistSerializer, RegistrationSerializer
# from rest_framework import status


@api_view(['GET','POST'])
@permission_classes([allCanGETButStaffOrAuthenticatedOnlyPOST])
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
    
class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email
            }
        else:
            data=serializer.errors

        return Response(data)
    

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            token = Token.objects.get_or_create(user=saved_account)
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email
            }
        else:
            data=serializer.errors

        return Response(data)