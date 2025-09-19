# Cyber News 2025 🛡️

A modern Flask web application for tracking and displaying cybersecurity-related news using real news APIs. This application provides a clean, responsive interface for staying updated with the latest security threats, data breaches, and technology news.

![Homepage Screenshot](https://github.com/user-attachments/assets/7f6ffd1f-d06c-4ec7-bf25-2e9cb2fc9cbf)

## Features

### 🏠 **Main News Feed**
- Fetches real-time cybersecurity news from NewsAPI
- Clean, responsive card-based layout
- Multiple topic categories (cybersecurity, technology, data breach, hacking)
- Article bookmarking functionality
- Auto-refresh capability
- Mobile-friendly design

### 🔐 **Admin Dashboard**
![Admin Dashboard](https://github.com/user-attachments/assets/edd5dd8d-7a46-47f5-97e9-fe3bf8a1afcc)

- Protected admin interface with login authentication
- Configure news topics and keywords
- Manage display settings (max articles, refresh intervals)
- Control preferred news sources
- System status monitoring
- Export/import configuration

### 🎨 **Enhanced Features**
- **Bookmark System**: Save articles for later reading
- **Topic Filtering**: Browse by specific cybersecurity topics
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Real-time Updates**: Auto-refresh news feed
- **Clean UI**: Modern Bootstrap-based interface
- **Admin Controls**: Complete configuration management

## Quick Start

### Prerequisites
- Python 3.11+
- NewsAPI key (free from [newsapi.org](https://newsapi.org/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/maryambueck-web/Cyber_news_2025.git
   cd Cyber_news_2025
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your NewsAPI key
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser to `http://localhost:5000`
   - Admin login: username `admin`, password `admin123`

## Deployment on Replit

This application is ready for deployment on [Replit](https://replit.com/):

1. Create a new Python Replit project
2. Upload all files or connect to this GitHub repository
3. The application will run automatically using `main.py`
4. Access your deployed site at your Replit URL
5. Enable "Always On" in the settings for 24/7 availability

### Replit Configuration
- Uses `main.py` as entry point
- Configured with `host="0.0.0.0", port=81`
- Includes `.replit` configuration file
- Poetry support with `pyproject.toml`

## Configuration

### Environment Variables
- `NEWS_API_KEY`: Your NewsAPI key for live data
- `SECRET_KEY`: Flask secret key for sessions

### Admin Settings
Access the admin dashboard at `/admin` to configure:
- **Topics**: Keywords used for news searches
- **Display Settings**: Number of articles, refresh intervals
- **News Sources**: Preferred sources to prioritize
- **System Status**: Monitor API connections and cache

## Project Structure

```
Cyber_news_2025/
├── app.py                 # Main Flask application
├── main.py               # Replit entry point
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .replit              # Replit configuration
├── templates/           # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Homepage
│   ├── login.html      # Admin login
│   └── admin.html      # Admin dashboard
├── static/             # Static assets
│   ├── css/style.css   # Custom styles
│   └── js/app.js       # JavaScript functionality
└── README.md           # This file
```

## API Integration

### NewsAPI
- Fetches real-time news articles
- Supports multiple topics and sources
- Fallback to sample data when API key is not available
- Rate limiting and error handling included

### Future Enhancements
- Additional news sources (RSS feeds, web scraping)
- Database storage for articles and user preferences
- User accounts with personalized feeds
- Advanced filtering and search capabilities

## Development

### Running in Development Mode
```bash
python app.py
```
The application runs with debug mode enabled and auto-reload.

### Testing Features
1. **News Feed**: Visit homepage to see articles
2. **Admin Panel**: Login with `admin`/`admin123`
3. **Configuration**: Test topic and settings updates
4. **Bookmarks**: Try bookmarking articles
5. **Responsive**: Test on different screen sizes

## Technologies Used

- **Backend**: Flask, Python 3.11+
- **Frontend**: Bootstrap 5, JavaScript ES6
- **APIs**: NewsAPI for live news data
- **Authentication**: Flask-Login
- **Styling**: Custom CSS with Bootstrap
- **Deployment**: Replit-ready configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is created for educational purposes as part of a cybersecurity news aggregation assignment.

## Support

For questions or issues:
1. Check the admin dashboard for system status
2. Verify your NewsAPI key is valid
3. Review browser console for any errors
4. Test with different topics and sources

---

**Built with ❤️ using Flask and NewsAPI** | **Stay updated with the latest cybersecurity news!**
