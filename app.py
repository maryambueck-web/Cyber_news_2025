#!/usr/bin/env python3
"""
Cyber News Tracker - Main Flask Application
A web application to track and display cybersecurity-related news using NewsAPI
"""

import os
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
from cyber_news.services.news_service import NewsService

# Load environment variables
load_dotenv()

def create_app():
    """Application factory pattern"""
    app = Flask(__name__, 
                template_folder='cyber_news/templates',
                static_folder='cyber_news/static')
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')
    app.config['NEWSAPI_KEY'] = os.getenv('NEWSAPI_KEY')
    
    # Initialize services
    news_service = NewsService(app.config['NEWSAPI_KEY'])
    
    # Admin credentials (in production, use proper authentication)
    ADMIN_USERS = {
        os.getenv('ADMIN_USERNAME', 'admin'): generate_password_hash(os.getenv('ADMIN_PASSWORD', 'admin'))
    }
    
    @app.route('/')
    def index():
        """Main dashboard showing latest cyber news"""
        try:
            # Get latest cybersecurity news
            news_articles = news_service.get_cyber_news()
            return render_template('index.html', articles=news_articles)
        except Exception as e:
            flash(f'Error fetching news: {str(e)}', 'error')
            return render_template('index.html', articles=[])
    
    @app.route('/search')
    def search():
        """Search for specific cybersecurity topics"""
        query = request.args.get('q', '')
        page = request.args.get('page', 1, type=int)
        
        if not query:
            return render_template('search.html', articles=[], query='')
        
        try:
            articles = news_service.search_news(query, page=page)
            return render_template('search.html', articles=articles, query=query, page=page)
        except Exception as e:
            flash(f'Search error: {str(e)}', 'error')
            return render_template('search.html', articles=[], query=query)
    
    @app.route('/admin/login', methods=['GET', 'POST'])
    def admin_login():
        """Admin login page"""
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            if username in ADMIN_USERS and check_password_hash(ADMIN_USERS[username], password):
                session['admin_logged_in'] = True
                session['admin_username'] = username
                flash('Successfully logged in!', 'success')
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid credentials!', 'error')
        
        return render_template('admin/login.html')
    
    @app.route('/admin/logout')
    def admin_logout():
        """Admin logout"""
        session.pop('admin_logged_in', None)
        session.pop('admin_username', None)
        flash('Logged out successfully!', 'info')
        return redirect(url_for('index'))
    
    @app.route('/admin')
    def admin_dashboard():
        """Admin dashboard"""
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        
        try:
            # Get some stats for the dashboard
            recent_articles = news_service.get_cyber_news(page_size=5)
            stats = {
                'total_sources': len(news_service.get_sources()),
                'recent_articles': len(recent_articles),
                'api_status': 'Connected' if news_service.test_connection() else 'Error'
            }
            return render_template('admin/dashboard.html', stats=stats, recent_articles=recent_articles)
        except Exception as e:
            flash(f'Dashboard error: {str(e)}', 'error')
            return render_template('admin/dashboard.html', stats={}, recent_articles=[])
    
    @app.route('/api/news')
    def api_news():
        """API endpoint for news data"""
        try:
            category = request.args.get('category', 'cybersecurity')
            page = request.args.get('page', 1, type=int)
            
            articles = news_service.get_cyber_news(category=category, page=page)
            return jsonify({
                'success': True,
                'articles': articles,
                'page': page
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.errorhandler(404)
    def not_found(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)