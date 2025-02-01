## HNG Stage 0 Task - Django API

This project is a simple Django API that returns basic information, including:
- A registered email address.
- The current UTC datetime in ISO 8601 format.
- The GitHub URL of the project.

## Features
- **Simple API**: Returns a JSON response with the required information.
- **Dynamic Datetime**: The `current_datetime` field is generated dynamically in UTC.
- **CORS Support**: Handles Cross-Origin Resource Sharing (CORS) for frontend compatibility.

## Setup Instructions
## 1️⃣ Clone the Repository
`
git clone https://github.com/yourusername/your-repo.git
cd your-repo
`
## 2️⃣ Install Dependencies
Make sure you have Python installed, then run:
`pip install django`

## 3️⃣ Create a Django Project
`django-admin startproject hng_stage0`
`cd hng_stage0`

## 4️⃣ Create a Django App
`python manage.py startapp api`

## 5️⃣ Add the App to Installed Apps

Open hng_stage0/settings.py and add 'api' to the INSTALLED_APPS list:

`INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',  # Add this line
]`

## 6️⃣ Write the API Code

➤ Create a View

Open api/views.py and add the following code:

```
from django.http import JsonResponse
from datetime import datetime'
 
 def get_info(request):
    email = "your-email@example.com"  # Replace with your registered email
    current_datetime = datetime.utcnow().isoformat() + "Z"
    github_url = "https://github.com/yourusername/your-repo"  # Replace with your GitHub URL
    response = {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }
    return JsonResponse(response)
```
    
➤ Define the URL Path

Create a file api/urls.py (if it doesn’t exist) and add:
  
  ```
  from django.urls import path
  from .views import get_info
  
  urlpatterns = [
      path('api/', get_info, name='get_info'),
  ]
  ```

➤ Include the App URLs in the Project

Open hng_stage0/urls.py and modify it as follows:

  ```
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('api.urls')),  # Include API routes
  ]
```

## 7️⃣ Run the Server

`python manage.py runserver`

Your API should now be accessible at:

`http://127.0.0.1:8000/api/`

📄 Sample API Response

If you visit http://127.0.0.1:8000/api/, you should get a response like this:

  ```
  {
      "email": "your-email@example.com",
      "current_datetime": "2025-01-31T12:00:00Z",
      "github_url": "https://github.com/yourusername/your-repo"
  }
  ```


## 🎯 Contributing

Feel free to fork this repository, create a new branch, and submit a pull request! Contributions are welcome.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🔗 Backlink

[HNG Python Developers](https://hng.tech/hire/python-developers)
