import os
import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Simple user class for admin authentication
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id == '1':  # Simple admin user
        return User(user_id)
    return None

# Configuration storage (in production, use a database)
app_config = {
    'topics': ['cybersecurity', 'technology', 'data breach', 'hacking'],
    'max_articles': 10,
    'refresh_interval': 30,  # minutes
    'news_sources': ['techcrunch', 'wired', 'ars-technica']
}

def get_news_api_key():
    """Get NewsAPI key from environment or return demo key"""
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        # Using a demo key for testing - replace with actual key
        api_key = 'demo_key'
    return api_key

def fetch_news_articles(query='cybersecurity', page_size=10):
    """Fetch news articles from NewsAPI"""
    api_key = get_news_api_key()
    
    # If no API key is available, return sample data
    if api_key == 'demo_key':
        return get_sample_news_data()
    
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'sortBy': 'publishedAt',
        'pageSize': page_size,
        'apiKey': api_key,
        'language': 'en'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('articles', [])
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        return get_sample_news_data()

def get_sample_news_data():
    """Return sample cybersecurity news data for demo purposes"""
    return [
        {
            'title': 'Major Data Breach Affects Millions of Users',
            'description': 'A significant cybersecurity incident has compromised personal data of millions of users across multiple platforms.',
            'url': 'https://example.com/news/data-breach',
            'urlToImage': 'https://via.placeholder.com/300x200?text=Cybersecurity+News',
            'publishedAt': '2024-01-15T10:30:00Z',
            'source': {'name': 'Tech Security News'}
        },
        {
            'title': 'New AI-Powered Threat Detection System Launched',
            'description': 'Companies are now deploying advanced AI systems to detect and prevent sophisticated cyber attacks in real-time.',
            'url': 'https://example.com/news/ai-security',
            'urlToImage': 'https://via.placeholder.com/300x200?text=AI+Security',
            'publishedAt': '2024-01-14T14:20:00Z',
            'source': {'name': 'Cyber Defense Weekly'}
        },
        {
            'title': 'Ransomware Attacks Target Healthcare Systems',
            'description': 'Recent surge in ransomware attacks specifically targeting healthcare infrastructure raises serious concerns.',
            'url': 'https://example.com/news/healthcare-ransomware',
            'urlToImage': 'https://via.placeholder.com/300x200?text=Healthcare+Security',
            'publishedAt': '2024-01-13T09:15:00Z',
            'source': {'name': 'Healthcare IT Security'}
        }
    ]

@app.route('/')
def index():
    """Main page displaying cybersecurity news"""
    query = request.args.get('topic', 'cybersecurity')
    articles = fetch_news_articles(query, app_config['max_articles'])
    
    # Format published dates
    for article in articles:
        if article.get('publishedAt'):
            try:
                dt = datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00'))
                article['formatted_date'] = dt.strftime('%B %d, %Y at %I:%M %p')
            except:
                article['formatted_date'] = 'Recently'
    
    return render_template('index.html', articles=articles, current_topic=query, topics=app_config['topics'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Simple admin login"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple hardcoded admin credentials (use proper authentication in production)
        if username == 'admin' and password == 'admin123':
            user = User('1')
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """Logout admin user"""
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin_dashboard():
    """Admin dashboard for configuration"""
    return render_template('admin.html', config=app_config)

@app.route('/admin/update', methods=['POST'])
@login_required
def update_config():
    """Update app configuration"""
    try:
        data = request.get_json()
        
        if 'topics' in data:
            app_config['topics'] = [topic.strip() for topic in data['topics'] if topic.strip()]
        
        if 'max_articles' in data:
            app_config['max_articles'] = max(1, min(50, int(data['max_articles'])))
        
        if 'refresh_interval' in data:
            app_config['refresh_interval'] = max(5, int(data['refresh_interval']))
        
        if 'news_sources' in data:
            app_config['news_sources'] = [source.strip() for source in data['news_sources'] if source.strip()]
        
        return jsonify({'status': 'success', 'message': 'Configuration updated successfully'})
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/api/articles')
def api_articles():
    """API endpoint to fetch articles"""
    topic = request.args.get('topic', 'cybersecurity')
    limit = min(int(request.args.get('limit', 10)), 50)
    
    articles = fetch_news_articles(topic, limit)
    return jsonify({
        'articles': articles,
        'total': len(articles),
        'topic': topic
    })

if __name__ == '__main__':
    # For Replit deployment
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)