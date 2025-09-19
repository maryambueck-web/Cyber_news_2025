# Cyber_news_2025
track and display cyber-related news using a real news API and build dynamic web apps with Flask :)
# 🛡️ CyberNews 2025

A dynamic Flask web application that tracks and displays cybersecurity-related news using real news APIs. Stay informed about the latest cyber threats, data breaches, malware, and security updates.

## 🌟 Features

- **Real-time News**: Fetches latest cybersecurity news from multiple APIs
- **Category Filtering**: Browse news by categories (Data Breaches, Malware, Ransomware, Vulnerabilities)
- **Smart Search**: Search for specific cybersecurity topics with intelligent filtering
- **Responsive Design**: Mobile-friendly interface with Bootstrap
- **API Endpoint**: JSON API for programmatic access to news data
- **Error Handling**: Graceful fallback to sample data when APIs are unavailable
- **Modern UI**: Clean, professional design with Font Awesome icons

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/maryambueck-web/Cyber_news_2025.git
cd Cyber_news_2025
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the `.env` file and add your API keys:

```bash
cp .env .env.local
```

Edit `.env` with your API keys:

```env
# Get your free API key from: https://newsapi.org/
NEWS_API_KEY=your_actual_news_api_key_here

# Optional: Guardian API key from: https://open-platform.theguardian.com/access/
GUARDIAN_API_KEY=your_guardian_api_key_here

# Flask configuration
SECRET_KEY=your_secret_key_for_production
FLASK_ENV=development
```

### 5. Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## 📁 Project Structure

```
Cyber_news_2025/
├── app.py                 # Main Flask application
├── news_service.py        # News API service module
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (template)
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── search.html       # Search page
│   ├── category.html     # Category pages
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Custom CSS styles
    └── js/
        └── main.js       # JavaScript functionality
```

## 🔧 API Configuration

### NewsAPI (Primary Source)

1. Visit [NewsAPI.org](https://newsapi.org/)
2. Sign up for a free account
3. Get your API key
4. Add it to your `.env` file as `NEWS_API_KEY`

### Guardian API (Optional Secondary Source)

1. Visit [Guardian Open Platform](https://open-platform.theguardian.com/access/)
2. Register for an API key
3. Add it to your `.env` file as `GUARDIAN_API_KEY`

**Note**: The app works with sample data if no API keys are configured, but all "Read More" buttons now link to real cybersecurity articles from trusted sources like SecurityWeek, Dark Reading, BleepingComputer, and others.

## 🌐 Available Routes

- `/` - Home page with latest cybersecurity news
- `/search?q=<query>` - Search for specific topics
- `/categories/<category>` - Category-specific news
  - `/categories/data-breach` - Data breach news
  - `/categories/malware` - Malware news
  - `/categories/ransomware` - Ransomware news
  - `/categories/vulnerability` - Vulnerability news
- `/api/news` - JSON API endpoint for programmatic access

## 🔍 Usage Examples

### Search Examples
- Search for "ransomware" to find ransomware-related news
- Search for "data breach" to find data breach incidents
- Search for "vulnerability" to find security vulnerabilities

### API Usage
```bash
# Get latest news in JSON format
curl http://localhost:5001/api/news

# Example response
{
  "status": "success",
  "data": [
    {
      "title": "Major Data Breach Affects Millions",
      "description": "A significant cybersecurity incident...",
      "url": "https://www.securityweek.com/major-data-breach-affects-millions/",
      "publishedAt": "2025-09-19T10:30:00Z",
      "source": {"name": "SecurityWeek"}
    }
  ]
}
```

### Real News Links ✨
**NEW**: All "Read More" buttons now connect to real cybersecurity articles from:
- 🔗 **SecurityWeek** - Enterprise security news
- 🔗 **Dark Reading** - Cybersecurity analysis  
- 🔗 **BleepingComputer** - Security incidents & malware
- 🔗 **The Hacker News** - Latest cyber threats
- 🔗 **Krebs on Security** - Investigative security journalism

### Quick Setup for Real News
```bash
# Run the setup helper
python setup_news.py

# For live API news, get a free key from NewsAPI:
# 1. Visit https://newsapi.org/
# 2. Sign up (free)
# 3. Add your key to .env file
# 4. Restart the app
```

## 🎨 Customization

### Adding New Categories

Edit `news_service.py` and add new categories to the `category_keywords` dictionary:

```python
self.category_keywords = {
    'data-breach': ['data breach', 'data leak'],
    'malware': ['malware', 'virus', 'trojan'],
    'your-category': ['keyword1', 'keyword2']
}
```

### Styling

Modify `static/css/style.css` to customize the appearance. The app uses Bootstrap 5 as the base framework.

## 🚀 Deployment

### Production Environment

1. Set environment variables:
```bash
export FLASK_ENV=production
export SECRET_KEY=your-secure-secret-key
```

2. Use a production WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Docker Deployment

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Troubleshooting

### Common Issues

**Issue**: "Command not found: pip"
**Solution**: Use the full Python path: `/path/to/your/venv/bin/python -m pip install -r requirements.txt`

**Issue**: No news articles showing
**Solution**: Check your API keys in the `.env` file. The app shows sample data if APIs are unavailable.

**Issue**: Import errors
**Solution**: Make sure you're in the virtual environment: `source .venv/bin/activate`

### Getting Help

- Open an issue on GitHub for bugs or feature requests
- Check the logs in your terminal for error messages
- Ensure all dependencies are installed: `pip list`

## 🔮 Future Enhancements

- [ ] User authentication and personalized news feeds
- [ ] Email notifications for critical security alerts
- [ ] Dark mode toggle
- [ ] News article sentiment analysis
- [ ] RSS feed generation
- [ ] Integration with threat intelligence feeds
- [ ] Mobile app with push notifications

---

**Built with ❤️ using Flask, Bootstrap, and cybersecurity news APIs**
