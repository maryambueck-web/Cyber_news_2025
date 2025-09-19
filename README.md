# Cyber News Tracker 2025

A Flask-based web application that tracks and displays cybersecurity-related news using the NewsAPI. Features a modern responsive interface, admin controls, and real-time news updates.

## 🚀 Features

- **Real-time News Tracking**: Fetches latest cybersecurity news from NewsAPI
- **Smart Categorization**: Automatically categorizes articles (Data Breach, Malware, Vulnerability, etc.)
- **Advanced Search**: Search for specific cybersecurity topics and threats
- **Admin Dashboard**: Manage news sources, API settings, and view statistics
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional interface with Bootstrap 5
- **API Integration**: RESTful endpoints for news data
- **Error Handling**: Graceful fallbacks when API is unavailable

## 📋 Prerequisites

- Python 3.8 or higher
- NewsAPI key (free at [newsapi.org](https://newsapi.org))

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/maryambueck-web/Cyber_news_2025.git
   cd Cyber_news_2025
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your NewsAPI key:
   ```
   NEWSAPI_KEY=your_newsapi_key_here
   FLASK_SECRET_KEY=your_secret_key_here
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=your_secure_password
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Main dashboard: http://localhost:5000
   - Admin panel: http://localhost:5000/admin/login

## 🔧 Configuration

### NewsAPI Setup
1. Visit [newsapi.org](https://newsapi.org) and create a free account
2. Get your API key from the dashboard
3. Add it to your `.env` file as `NEWSAPI_KEY=your_key_here`
4. Restart the application

### Admin Access
- Default username: `admin`
- Default password: Set in `.env` file
- Change these credentials in production!

## 🌐 Deployment

### Heroku Deployment
1. Create a Heroku app
2. Set environment variables in Heroku dashboard
3. Deploy using Git or GitHub integration

### Manual Deployment
1. Set environment variables on your server
2. Install dependencies with `pip install -r requirements.txt`
3. Run with `python app.py` or use a WSGI server like Gunicorn

## 📱 API Endpoints

- `GET /` - Main dashboard
- `GET /search?q=<query>` - Search news articles
- `GET /api/news` - JSON API for news data
- `GET /admin` - Admin dashboard (requires authentication)

## 🎨 Creative Features

- **Smart Categorization**: Articles are automatically categorized based on content
- **Real-time Updates**: Dashboard refreshes every 5 minutes
- **Responsive Design**: Optimized for all device sizes
- **Search Suggestions**: Quick search tags for common cybersecurity topics
- **Admin Controls**: Manage settings and view system statistics

## 🔒 Security Features

- **Input Validation**: All user inputs are sanitized
- **Admin Authentication**: Secure admin panel access
- **Error Handling**: Graceful error handling and fallbacks
- **Environment Variables**: Sensitive data stored securely

## 🛡️ Cybersecurity Keywords Tracked

The application monitors news for these cybersecurity-related terms:
- Cybersecurity, Cyber Attack, Data Breach
- Malware, Ransomware, Phishing
- Hacking, Vulnerability, Zero-day
- DDoS, Firewall, Encryption
- And more...

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:
1. Check that your NewsAPI key is valid and not rate-limited
2. Ensure all dependencies are installed correctly
3. Check the application logs for error details
4. Open an issue on GitHub with error details

## 🌟 Acknowledgments

- [NewsAPI](https://newsapi.org) for providing the news data
- [Bootstrap](https://getbootstrap.com) for the responsive UI framework
- [Font Awesome](https://fontawesome.com) for the icons
- [Flask](https://flask.palletsprojects.com) for the web framework

---

**Built with ❤️ for cybersecurity awareness and education**
