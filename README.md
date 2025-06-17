# Task Manager
[![Actions Status](https://github.com/kazanmarat/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kazanmarat/python-project-52/actions)

Task Manager is a training project for creating a task management system. This web service ([Render](https://python-project-52-o0yq.onrender.com/)) makes it convenient to work with tasks. \
All visitors to the site initially have access only to a list of all registered users.

### After registration, additional options become available:
- Editing your profile. Changing or deleting information about yourself. If the user is the author or performer of a task, deleting it is not available;
- Viewing, adding, updating and deleting task statuses and labels after logging in. Statuses and labels corresponding to any tasks cannot be deleted;
- Managing tasks (viewing, adding, updating and deleting). You can assign a performer to a task. Only the creator can delete tasks. A task filter is also available on the corresponding page with filtering by status, performer, label and authorship.
 
The service works in Russian or English depending on the browser language. \
More information about such projects is written in [Wikipedia](https://en.wikipedia.org/wiki/Task_management). \
Task Manager is a task management system similar to [Redmine](http://www.redmine.org/).

## Installation
### Prerequisites
- Python version 3.10 or higher
- Django version 5.2 or higher
- PostgreSQL version 16.6 or higher
- Uv version 0.5.14 or higher (optional)

### Download
    git clone https://github.com/kazanmarat/python-project-52.git

### Set configuration
Prepare the database. \
Prepare the environment variables according to the `.env_example` file. \
`Makefile` simplifies the installation and startup process with the following commands:
### Build the application
    make build
#### Starting a server
    make start

