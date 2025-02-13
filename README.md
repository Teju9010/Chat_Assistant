Chat Assistant (Rasa)

Overview
This is a Rasa chatbot that interacts with an SQLite database to answer queries about employees and departments.

Features
- Supports natural language queries
- Fetches data from an SQLite database
- Handles user questions like:
  - "Who is the manager of Sales?"
  - "List all employees in Marketing."
  - "What is the total salary expense for Engineering?"
- Deployed using Flask API server
  
Installation & Setup

1.Clone the Repository
```
git clone https://github.com/Teju9010/chat-assistant.git
cd chat-assistant

2. Install dependancies
conda create --name Chat_Assistant 
conda activate Chat_Assistant
go to the required folder
pip install rasa rasa-sdk sqlite3
rasa init

3.rasa train # training the bot

4.rasa run actions #starting action server

5.rasa shell #starting the chatbot

6. rasa run --enable api
   python server.py # starting Flask server

7. testing api by
```curl -X POST "http://localhost:5000/chat" \
     -H "Content-Type: application/json" \
     -d "{\"message\": \"Who is the manager of Sales?\"}"
```

8.Expected response:
  [{"recipient_id": "user", "text": "The manager of Sales is Alice."}]

Known Limitations:
- Currently, only supports basic SQL queries.
- No authentication/security in API.
- Needs better error handling for invalid queries.

Future Improvements:
- Host on a VPS for public access.
- Improve NLP models for better query handling.
- Frontend UI (React/HTML) for better usability.
  
Open source project under the MIT License
© 2025 Sai Tejaswini - All rights reserved.
