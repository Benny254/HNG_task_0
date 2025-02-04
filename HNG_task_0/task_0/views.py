from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt

EMAIL = "asshimbenny01@gmail.com"
GITHUB_URL = "https://github.com/Benny254/HNG_task_0"

@csrf_exempt
def public_api(request):
    if request.method == "GET":
        response_data = {
            "email": EMAIL,
            "current_datetime": now().isoformat(),
            "github_url": GITHUB_URL
        }
        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

