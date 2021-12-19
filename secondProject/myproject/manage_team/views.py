import json
from json.decoder import JSONDecodeError

from django.http import JsonResponse
from django.views.generic import View, ListView, DetailView

from member.models import Member
from .models import Team


class ListTeamView(ListView):
    # 모든 팀 조회
    def get(self, request):
        teams = Team.objects.all()
        result = [{
            'id': team.pk,
            'name': team.name,
        } for team in teams]

        return JsonResponse({'data': result}, status=200)


class TeamView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data['name']

            if Team.objects.filter(name=name).exists():
                return JsonResponse({'message': '이미 해당 아이디의 팀이 있습니다'}, status=409)

            # 팀 저장
            Team(name=name).save()

            return JsonResponse({'message': '팀 생성 성공'}, status=200)
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class RegisterTeamView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_name = data['user_name']
            team_name = data['team_name']

            found_team = Team.objects.get(name=team_name)
            found_member = Member.objects.get(name=user_name)

            found_member.team = found_team

            # 팀 저장
            found_member.save()

            return JsonResponse({'message': '팀 등록 성공'}, status=200)

        except Team.DoesNotExist:
            return JsonResponse({'message': '해당 팀 없습니다'}, status=404)
        except Member.DoesNotExist:
            return JsonResponse({'message': '해당 유저 없습니다'}, status=404)
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class DeleteTeamView(View):
    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
            team.delete()
            return JsonResponse({'message': '팀 삭제 성공'}, status=200)

        except Team.DoesNotExist:
            return JsonResponse({'message': '해당 아이디의 팀이 없습니다'}, status=404)


class MembersView(View):
    def get(self, request, team_id):
        if request.method == 'GET':
            found_members = Member.objects.filter(team_id=team_id)

            result = [{
                'id': member.pk,
                'name': member.name,
                'age': member.age,
            } for member in found_members]

            return JsonResponse({'data': result}, status=200)
