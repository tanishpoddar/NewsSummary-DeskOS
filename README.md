# News Summary App

A Django + Vanilla JS web application for user-authenticated news aggregation, summarization, and saving favorite articles. News is fetched from NewsAPI and summarized using Gemini API.

## Features
- User registration and JWT-based authentication
- Fetch and summarize latest news headlines
- Search and summarize news by query
- Save favorite news articles (per user)
- Responsive, single-page frontend (HTML/CSS/JS)
- No Django admin or superuser features

## Project Structure
```
DeskOS/
├── manage.py
├── db.sqlite3
├── news/                # Django app for news logic
│   ├── models.py        # Data models
│   ├── serializers.py   # DRF serializers
│   ├── views.py         # API endpoints
│   ├── urls.py          # App URL routing
│   ├── utils.py         # NewsAPI & Gemini utilities
│   ├── tests.py         # Test suite
│   └── ...
├── newsapi_project/     # Django project config
│   ├── settings.py      # Project settings
│   ├── urls.py          # Root URL routing
│   └── static/
│       └── index.html   # Responsive SPA frontend
└── requirements.txt     # Python dependencies
```

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set environment variables**
   - `NEWSAPI_KEY`: Your NewsAPI key
   - `GEMINI_API_KEY`: (Optional) Your Gemini API key (default is provided, but you should use your own for production)
   - You can use a `.env` file in the project root.
4. **Run migrations**
   ```bash
   python manage.py migrate
   ```
5. **Start the server**
   ```bash
   python manage.py runserver
   ```
6. **Access the app**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## API Endpoints
All endpoints require JWT authentication except registration and login.

| Endpoint                  | Method | Description                       |
|--------------------------|--------|-----------------------------------|
| `/api/auth/register/`    | POST   | Register a new user               |
| `/api/auth/login/`       | POST   | Obtain JWT token                  |
| `/api/auth/token/refresh/`| POST  | Refresh JWT token                 |
| `/api/news/latest/`      | GET    | Get summarized latest news        |
| `/api/news/search/?q=...`| GET    | Search and summarize news         |
| `/api/news/save/`        | POST   | Save a news article               |
| `/api/news/saved/`       | GET    | List saved news articles          |

## Frontend Usage
- The app is a single-page application (SPA) served at `/`.
- Navigation is responsive and updates the browser URL for each section.
- Login/Register are hidden when logged in; Latest/Search/Saved/Logout are hidden when logged out.
- Latest news is cached per session for efficiency.

## Testing
- Run tests with:
  ```bash
  python manage.py test
  ```