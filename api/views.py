
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from datetime import datetime,timezone
from datetime import datetime
import pytz

utc_plus_one = pytz.timezone('Europe/Amsterdam') 

@csrf_exempt
@require_GET
def get_info(request):
    
    email = "Kolademodupe007@gmail.com"  
    current_datetime = datetime.now(utc_plus_one)
    github_url = "https://github.com/dartlord007/hng_stage0"  

    response = {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }

    return JsonResponse(response)