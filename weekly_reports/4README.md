Week 4 Update Authentication & Authorization

This week, I implemented *JWT authentication* to secure the Task Management API.

New updates:
1. Created a 'users' app for handling user registration and authentication.  
2. Integrated SimpleJWT for issuing and verifying access tokens.  
3. Updated API endpoints to require authentication for all task operations.  
4. Users can now:
  a. Register a new account via '/api/auth/register/'
  b. Log in via '/api/auth/login/' to get access and refresh tokens
  c. Refresh their token via '/api/auth/refresh/`

All task endpoints are now protected users must include their access token in the 'Authorization' header:
