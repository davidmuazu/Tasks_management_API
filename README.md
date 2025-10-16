Task Management API

A simple backend project built with Django REST Framework for managing tasks.  
Users can register, log in, and create tasks that are linked to their account.  
Each task can be marked as complete or incomplete.

Task management api Features
- User registration and JWT-based authentication  
- Create, read, update, and delete tasks  
- Mark tasks as complete/incomplete  
- Each user only sees their own tasks  


Login to get Token
    POST → http://127.0.0.1:8000/api/auth/login/
    Body JSON:

 { "username": "demo_user", "password": "demo_password" }


List Tasks
    GET → http://127.0.0.1:8000/api/tasks/
     header:

 Authorization: Bearer <your_token_here>


 Create a Task
    POST → http://127.0.0.1:8000/api/tasks/
    Body JSON:

 { 
 
  "title": "Finish my workshop project",
  "description": "Roundup my school side project i've been working on",
  "is_completed": false
 }


Update and Complete
    PUT → http://127.0.0.1:8000/api/tasks/1/

Body JSON:

 {
  "title": "Record capstone presentation",
  "description": "Presentation video completed",
  "is_completed": true
}


Delete
    DELETE → http://127.0.0.1:8000/api/tasks/1/