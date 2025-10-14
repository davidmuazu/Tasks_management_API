Week 2: Environment and Authentication Setup

Objective: Build a secure foundation for user management and authentication.

Key Activities:

Created a virtual environment and ensured all dependencies were installed within it.

Installed and configured djangorestframework-simplejwt for JWT authentication.

Created a new app named users to handle user registration and login.

Defined serializers, views, and URLs for:

User registration (/api/auth/register/)

JWT login and token refresh (/api/auth/login/, /api/auth/refresh/)

Linked authentication routes in the main config/urls.py.

Outcome:
A working authentication system where users can register, log in, and receive JWT tokens for secure access.