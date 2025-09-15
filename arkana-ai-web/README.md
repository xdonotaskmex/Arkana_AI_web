# ARKANA AI Landing Page

This is the static landing page for ARKANA AI, hosted on GitHub Pages.

## Deployment

To deploy this landing page on GitHub Pages, you have two options:

### Option 1: Automatic Deployment with GitHub Actions (Recommended)

This repository includes a GitHub Actions workflow that automatically deploys the landing page to GitHub Pages whenever changes are made to the `docs` folder:

1. The workflow is defined in `.github/workflows/deploy-landing-page.yml`
2. It automatically triggers on pushes to the main branch that modify files in the `docs` folder
3. No manual configuration is needed - it works out of the box!

### Option 2: Manual Configuration

If you prefer to configure GitHub Pages manually:

1. Go to your repository settings
2. Scroll down to the "GitHub Pages" section
3. Under "Source", select "Deploy from a branch"
4. Choose the branch (usually `main` or `master`)
5. Select the `docs` folder as the source
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

1. Make changes to the files in this `docs` folder
2. Commit and push your changes to GitHub
3. If using GitHub Actions, the site will automatically deploy
4. If using manual configuration, GitHub Pages will automatically rebuild and deploy your site

## Files

- `index.html` - Main landing page
- `styles.css` - Custom styling
- `script.js` - JavaScript functionality
- `README.md` - This file

## Dependencies

All dependencies are loaded via CDN:
- Bootstrap 5.3
- AOS (Animate On Scroll)
- Feather Icons
- Three.js (for Vanta.js)
- Vanta.js Globe effect

No local installation is required for these dependencies.