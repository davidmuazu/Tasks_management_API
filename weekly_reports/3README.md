Week 3: Task App and Model Creation

Objective: Implement task-related features and data structure.

Key Activities:

Created a new Django app named tasks.

Designed an Entity Relationship Diagram (ERD) for User and Task models.

Implemented the Task model with fields:

title

description

is_completed

created_at

updated_at

user (ForeignKey to User)

Created serializers and basic views for CRUD operations.

Added API endpoints for tasks in tasks/urls.py:

/api/tasks/ → List & Create tasks

/api/tasks/<id>/ → Retrieve, Update, Delete task

Outcome:
The core task management features (CRUD) were implemented and integrated into the project.