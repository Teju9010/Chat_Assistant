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

Installation & Setup

1.Clone the Repository
```
git clone https://github.com/tejaswini/chat-assistant.git
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

```


