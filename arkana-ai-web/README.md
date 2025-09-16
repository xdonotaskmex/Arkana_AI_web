# ARKANA AI Landing Page

This is the static landing page for ARKANA AI, a Telegram-based financial analysis bot for cryptocurrency trading. The site is hosted on GitHub Pages.

## About ARKANA AI

ARKANA AI is an advanced financial analysis tool that provides AI-powered insights for cryptocurrency trading. With specialized AI personas, real-time technical analysis, and professional-grade charts, ARKANA AI helps traders make informed decisions in the volatile crypto market.

### Key Features

- **AI-Powered Analysis**: Six specialized AI personas provide unique perspectives on market trends
- **Technical Analysis**: Comprehensive technical indicators and Fibonacci levels
- **Real-time Data**: Cryptocurrency market data from CoinGecko API
- **Visual Charts**: Professional-grade technical charts with Plotly and matplotlib
- **News Analysis**: Financial news analysis using Tavily API to understand market sentiment
- **Premium Features**: Subscription-based access to advanced personas and unlimited analyses

## Recent Enhancements

### SEO Improvements
- Added comprehensive meta descriptions for better search engine visibility
- Implemented Open Graph and Twitter Card meta tags for social sharing
- Optimized keywords for cryptocurrency trading and AI analysis

### Dark Futuristic Theme
- Implemented a premium dark theme with deep navy blue background (#0d141f)
- Added glowing neon accents in cyan (#4cc9f0) and purple (#9d4edd)
- Integrated metallic gradient elements blending silver (#cccccc), cyan, and purple
- Updated typography to use futuristic geometric fonts (Orbitron for titles, Rajdhani for text)
- Added smooth glass-like cards with blurred dark backgrounds and neon glow edges
- Implemented background with subtle animated futuristic grid lines
- Enhanced overall look to be premium, AI-powered, mysterious and high-tech

## Deployment

To deploy this landing page on GitHub Pages, you have two options:

### Option 1: Automatic Deployment with GitHub Actions (Recommended)

This repository includes a GitHub Actions workflow that automatically deploys the landing page to GitHub Pages whenever changes are made to the `arkana-ai-web` folder:

1. The workflow is defined in `.github/workflows/deploy-landing-page.yml`
2. It automatically triggers on pushes to the main branch that modify files in the `arkana-ai-web` folder
3. No manual configuration is needed - it works out of the box!

### Option 2: Manual Configuration

If you prefer to configure GitHub Pages manually:

1. Go to your repository settings
2. Scroll down to the "GitHub Pages" section
3. Under "Source", select "Deploy from a branch"
4. Choose the branch (usually `main` or `master`)
5. Select the `arkana-ai-web` folder as the source
6. Click "Save"
7. Your site will be available at `https://[username].github.io/[repository-name]/`

## Custom Domain

To use a custom domain:

1. In your repository settings, go to the "GitHub Pages" section
2. In the "Custom domain" field, enter your domain name
3. Click "Save"
4. Configure your domain provider to point to your GitHub Pages site:
   - For an apex domain (example.com), create an A record pointing to:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - For a subdomain (www.example.com), create a CNAME record pointing to [username].github.io

## Updating the Site

To update the landing page:

1. Make changes to the files in the `arkana-ai-web` folder
2. Commit and push your changes to GitHub
3. If using GitHub Actions, the site will automatically deploy
4. If using manual configuration, GitHub Pages will automatically rebuild and deploy your site

## Project Structure

- `index.html` - Main landing page
- `styles.css` - Custom styling
- `script.js` - JavaScript functionality
- `404.html` - Error page
- `README.md` - This file

## Dependencies

All dependencies are loaded via CDN:
- Bootstrap 5.3
- AOS (Animate On Scroll)
- Feather Icons
- Three.js (for Vanta.js)
- Vanta.js Globe effect

No local installation is required for these dependencies.

## Browser Support

The landing page is designed to work on modern browsers:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For support or inquiries about ARKANA AI, please contact the project maintainers or visit our Telegram bot.