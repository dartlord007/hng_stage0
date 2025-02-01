
from django.http import JsonResponse
from datetime import datetime
import pytz

utc_plus_one = pytz.timezone('Europe/Amsterdam') 

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