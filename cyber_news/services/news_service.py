"""
News Service for fetching cybersecurity-related news from NewsAPI
"""

import requests
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class NewsService:
    """Service class for handling news API operations"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"
        self.headers = {"X-API-Key": api_key}
        
        # Cybersecurity-related keywords
        self.cyber_keywords = [
            "cybersecurity", "cyber attack", "data breach", "malware", 
            "ransomware", "phishing", "hacking", "vulnerability",
            "security breach", "cyber threat", "infosec", "penetration testing",
            "zero-day", "DDoS", "firewall", "encryption", "cyber crime"
        ]
    
    def test_connection(self) -> bool:
        """Test if the NewsAPI connection is working"""
        try:
            response = requests.get(
                f"{self.base_url}/sources",
                headers=self.headers,
                timeout=10
            )
            return response.status_code == 200
        except Exception:
            return False
    
    def get_sources(self) -> List[Dict]:
        """Get available news sources"""
        try:
            response = requests.get(
                f"{self.base_url}/sources",
                headers=self.headers,
                params={
                    "category": "technology",
                    "language": "en"
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get("sources", [])
            else:
                return []
        except Exception as e:
            print(f"Error fetching sources: {e}")
            return []
    
    def get_cyber_news(self, category: str = "cybersecurity", page: int = 1, page_size: int = 20) -> List[Dict]:
        """Get cybersecurity-related news articles"""
        try:
            # Build search query with cyber keywords
            query = " OR ".join(self.cyber_keywords[:5])  # Limit to avoid too long URL
            
            # Get articles from the last 7 days
            from_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            
            response = requests.get(
                f"{self.base_url}/everything",
                headers=self.headers,
                params={
                    "q": query,
                    "language": "en",
                    "sortBy": "publishedAt",
                    "from": from_date,
                    "page": page,
                    "pageSize": page_size
                },
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articles", [])
                
                # Process articles to add additional info
                processed_articles = []
                for article in articles:
                    processed_article = self._process_article(article)
                    if processed_article:
                        processed_articles.append(processed_article)
                
                return processed_articles
            else:
                print(f"NewsAPI error: {response.status_code} - {response.text}")
                return self._get_sample_articles()  # Fallback to sample data
                
        except Exception as e:
            print(f"Error fetching cyber news: {e}")
            return self._get_sample_articles()  # Fallback to sample data
    
    def search_news(self, query: str, page: int = 1, page_size: int = 20) -> List[Dict]:
        """Search for news articles with custom query"""
        try:
            # Add cybersecurity context to the search
            enhanced_query = f"({query}) AND (cybersecurity OR security OR cyber)"
            
            response = requests.get(
                f"{self.base_url}/everything",
                headers=self.headers,
                params={
                    "q": enhanced_query,
                    "language": "en",
                    "sortBy": "publishedAt",
                    "page": page,
                    "pageSize": page_size
                },
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                articles = data.get("articles", [])
                
                processed_articles = []
                for article in articles:
                    processed_article = self._process_article(article)
                    if processed_article:
                        processed_articles.append(processed_article)
                
                return processed_articles
            else:
                return []
                
        except Exception as e:
            print(f"Error searching news: {e}")
            return []
    
    def _process_article(self, article: Dict) -> Optional[Dict]:
        """Process and clean article data"""
        try:
            # Skip articles without essential information
            if not article.get("title") or not article.get("url"):
                return None
            
            # Parse and format the published date
            published_at = article.get("publishedAt", "")
            formatted_date = ""
            if published_at:
                try:
                    dt = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                    formatted_date = dt.strftime("%B %d, %Y at %I:%M %p")
                except:
                    formatted_date = published_at
            
            # Determine article category based on keywords
            content = f"{article.get('title', '')} {article.get('description', '')}"
            category = self._categorize_article(content)
            
            return {
                "title": article.get("title", ""),
                "description": article.get("description", ""),
                "url": article.get("url", ""),
                "urlToImage": article.get("urlToImage", ""),
                "publishedAt": formatted_date,
                "source": article.get("source", {}).get("name", "Unknown"),
                "category": category,
                "author": article.get("author", "")
            }
        except Exception as e:
            print(f"Error processing article: {e}")
            return None
    
    def _categorize_article(self, content: str) -> str:
        """Categorize article based on content"""
        content_lower = content.lower()
        
        if any(word in content_lower for word in ["ransomware", "malware", "virus"]):
            return "Malware"
        elif any(word in content_lower for word in ["data breach", "breach", "leaked"]):
            return "Data Breach"
        elif any(word in content_lower for word in ["phishing", "scam", "fraud"]):
            return "Phishing"
        elif any(word in content_lower for word in ["vulnerability", "exploit", "zero-day"]):
            return "Vulnerability"
        elif any(word in content_lower for word in ["ddos", "attack", "cyber attack"]):
            return "Cyber Attack"
        else:
            return "General Security"
    
    def _get_sample_articles(self) -> List[Dict]:
        """Fallback sample articles when API is not available"""
        return [
            {
                "title": "Major Cybersecurity Breach Affects Millions",
                "description": "A significant data breach has exposed personal information of millions of users worldwide, highlighting the importance of robust cybersecurity measures.",
                "url": "#",
                "urlToImage": "",
                "publishedAt": datetime.now().strftime("%B %d, %Y at %I:%M %p"),
                "source": "Sample News",
                "category": "Data Breach",
                "author": "Security Reporter"
            },
            {
                "title": "New Ransomware Strain Targets Healthcare Systems",
                "description": "Healthcare organizations worldwide are being targeted by a sophisticated ransomware campaign that encrypts critical patient data.",
                "url": "#",
                "urlToImage": "",
                "publishedAt": (datetime.now() - timedelta(hours=2)).strftime("%B %d, %Y at %I:%M %p"),
                "source": "CyberSec Daily",
                "category": "Malware",
                "author": "Health Security Team"
            },
            {
                "title": "Zero-Day Vulnerability Discovered in Popular Software",
                "description": "Security researchers have identified a critical zero-day vulnerability that could allow attackers to gain unauthorized access to systems.",
                "url": "#",
                "urlToImage": "",
                "publishedAt": (datetime.now() - timedelta(hours=5)).strftime("%B %d, %Y at %I:%M %p"),
                "source": "Tech Security News",
                "category": "Vulnerability",
                "author": "Research Team"
            }
        ]