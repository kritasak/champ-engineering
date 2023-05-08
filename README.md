# ChAMP Engineering Final Project - Backend

This is a Flask API for a board with lists and tasks.

## Requirements

To run this project locally, you will need to have the following tools installed:

- Python 3.6 or higher
- Flask

## Installation

1. Clone this repository:

```
git clone https://github.com/your-username/board-api.git
```

2. Navigate to the project directory:

```
cd board-api
```

3. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

To start the API, run the following command:

```
python app.py
```

The API should now be running at `http://localhost:5000`.

You can test the API using a tool like Postman or by sending HTTP requests directly to the API endpoints.

## API Endpoints

Here are the available API endpoints:

- GET /lists: Get a list of all lists
- POST /lists: Create a new list
- GET /lists/:list_id: Get a specific list
- PUT /lists/:list_id: Update a specific list
- DELETE /lists/:list_id: Delete a specific list and all tasks in it
- PUT /lists/:list_id/reorder: Reorder a specific list
- GET /tasks: Get a list of all tasks
- POST /tasks: Create a new task
- GET /tasks/:task_id: Get a specific task
- PUT /tasks/:task_id: Update a specific task
- DELETE /tasks/:task_id: Delete a specific task
- PUT /tasks/:task_id/move: Move a specific task to another list
- PUT /tasks/:task_id/reorder: Reorder a specific task in its list
