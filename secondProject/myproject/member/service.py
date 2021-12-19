from django.http import JsonResponse

from .models import Member


class MemberService:
    def signup(self, name: str, age: int):
        if Member.objects.filter(name=name).exists():
            return JsonResponse({'message': '이미 해당 이메일의 회원이 있습니다'}, status=409)

        Member(name=name, age=age).save()

        return JsonResponse({'message': '회원 생성 성공'}, status=200)

