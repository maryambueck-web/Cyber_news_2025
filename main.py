# main.py - Entry point for Replit deployment
from app import app

if __name__ == '__main__':
    # Configuration for Replit deployment
    app.run(host="0.0.0.0", port=81, debug=False)