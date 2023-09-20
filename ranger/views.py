from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .forms import NoteForm
from .models import Note, Menu, Case


class LogoutView(APIView):

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MenuListView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def serialize_menu(menu_ids):
        menus = {
            menu.id: menu
            for menu in Menu.objects.all()
        }

        menu_data = list()
        visited_menu = dict()

        for id in menu_ids:
            submenu = dict()
            done = False
            item = menus.get(id)
            endpoint = {
                'name': item.name,
                'url': item.url,
                'submenu': []
            }
            item = item.parent
            while item and not done:
                if visited_menu.get(item.id):
                    visited_menu.get(item.id)['submenu'].append(submenu if submenu else endpoint)
                    done = True
                else:
                    submenu = {
                        'name': item.name,
                        'url': item.url,
                        'submenu': [submenu] if submenu else [endpoint]
                    }
                    visited_menu[item.id] = submenu
                    if not item.parent:
                        menu_data.append(submenu)
                item = item.parent
        return menu_data

    def post(self, request):
        name = (request.data['case_name'])
        ids = Case.objects.get(name=name).menus
        menu_list = MenuListView.serialize_menu(ids)

        return Response(menu_list)


class NoteCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        case_name = request.data['case']
        form = NoteForm({
            "title": request.data["title"],
            "explanation": request.data["explanation"],
            "case": Case.objects.get(name=case_name)
        })
        if form.is_valid():
            note = form.save()
            return Response({'id': note.id}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        case_name = request.data['case']
        note_titles = request.data['notes']
        Note.objects.filter(case__name=case_name, title__in=note_titles).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteListView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        case_name = request.data['case']
        notesData = Note.objects.filter(case__name=case_name).order_by('-last_modified').values()
        return Response(notesData)


class CaseRetrieve(APIView):
    def get(self, request):
        cases = Case.objects.values_list('name', flat=True).order_by('name')
        return Response(list(cases))
