# Deployment Guide for Cyber News 2025

This guide covers the deployment steps specifically mentioned in the project requirements.

## Step 2: How to Deploy on Replit

### Quick Deployment Steps

1. **Create a new Python Replit project**
   - Go to [replit.com](https://replit.com/)
   - Click "Create Repl"
   - Select "Python" as the template
   - Name your project "cyber-news-2025"

2. **Upload your Flask code**
   - Delete the default `main.py` content
   - Copy all files from this repository to your Replit
   - The `main.py` file is already configured for Replit

3. **Configure for public access**
   - The app is already set to use `app.run(host="0.0.0.0", port=81)`
   - This makes it visible on the internet

4. **Enable "Always On"**
   - Click the ⚙️ (settings) button in the sidebar
   - Toggle "Always On" to keep your site running 24/7
   - Note: This may require a paid Replit plan

5. **Test from another device**
   - Click "Run" to start your application
   - Copy the public URL from Replit
   - Test the URL in a different browser or device

### Environment Setup on Replit

1. **Add your NewsAPI key** (Optional)
   - Get a free API key from [newsapi.org](https://newsapi.org/)
   - In Replit, go to the "Secrets" tab (lock icon)
   - Add a new secret: `NEWS_API_KEY` with your API key
   - The app works with sample data without an API key

2. **Files already configured for Replit:**
   - `main.py` - Entry point with correct host/port
   - `.replit` - Replit configuration
   - `pyproject.toml` - Poetry dependencies
   - `requirements.txt` - Pip dependencies

## What Your Deployed Site Includes

### ✅ Step 1: News Online (Complete)
- Connects to NewsAPI for live cybersecurity headlines
- Displays title, summary, and link for each article
- Clean, readable format in the browser
- Works with sample data even without API key

### ✅ Step 3: Admin Dashboard (Complete)
- Protected login interface (admin/admin123)
- Configure topics and keywords for NewsAPI requests
- Define additional API sources
- Control article count and refresh frequency
- Export/import configuration settings

### ✅ Step 4: Enhanced Features (Complete)
- **Article Tagging**: Articles are categorized by topic
- **Bookmark Functionality**: Save articles for later reading
- **Responsive Design**: Mobile-friendly and dark mode support
- **Topic Filtering**: Filter by cybersecurity, technology, data breach, hacking
- **User System**: Admin authentication with role-based access
- **Auto-refresh**: Configurable news feed updates

## Sharing Your Deployed Link

Once deployed on Replit, your site will have a URL like:
```
https://cyber-news-2025.your-username.repl.co
```

### For Final Submission Include:
1. **Your Replit URL** - The live, working site
2. **Admin credentials** - Username: `admin`, Password: `admin123`
3. **Features demonstration** - Show the admin panel and configuration options

## Testing Your Deployment

### Frontend Testing
- [ ] Homepage loads with news articles
- [ ] Topic filtering works (cybersecurity, technology, etc.)
- [ ] Responsive design on mobile devices
- [ ] Bookmark functionality works
- [ ] Auto-refresh countdown appears

### Admin Testing
- [ ] Login page accessible at `/login`
- [ ] Admin credentials work (admin/admin123)
- [ ] Admin dashboard loads at `/admin`
- [ ] Configuration updates work
- [ ] Export config functionality works

### API Testing
- [ ] Site works without API key (shows sample data)
- [ ] With API key, shows real news articles
- [ ] Error handling for API failures

## Troubleshooting

### Common Issues
1. **Site not loading**: Check if the Replit is running
2. **No articles showing**: Normal with demo data, or check API key
3. **Admin not working**: Verify credentials are admin/admin123
4. **Styling issues**: Check if Bootstrap CSS is loading

### Debug Steps
1. Check the Replit console for error messages
2. Open browser developer tools for JavaScript errors
3. Verify all files uploaded correctly
4. Test the `/api/articles` endpoint directly

## Performance Notes

- Sample data loads instantly
- Real NewsAPI calls may take 1-2 seconds
- Admin configuration updates are immediate
- Bookmark data stored in browser localStorage

---

Your Cyber News 2025 app is now ready for demonstration and submission! 🚀