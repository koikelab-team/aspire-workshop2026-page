# ASPIRE Workshop 2026 Website

A modern, professionally designed GitHub Pages site for the ASPIRE Workshop 2026.

## Features

- Modern academic blue color scheme
- Responsive design (mobile-friendly)
- Custom CSS styling with hover effects
- Placeholder sections for images and logos
- Professional card layouts for contact information
- Styled tables and information boxes

## Directory Structure

```
aspire-workshop2026-page/
├── index.md              # Main content file
├── _config.yml           # Jekyll configuration
├── assets/
│   ├── css/
│   │   └── style.scss    # Custom CSS styling
│   └── images/           # Place your images here
└── README.md             # This file
```

## Adding Images

### Venue Photos

1. Add your images to the `assets/images/` folder (e.g., `venue1.jpg`, `venue2.jpg`, `venue3.jpg`)

2. Replace the image placeholders in [index.md](index.md) (around line 93-106):

```markdown
<div class="image-gallery">
  <img src="assets/images/venue1.jpg" alt="Karuizawa Prince Hotel">
  <img src="assets/images/venue2.jpg" alt="Conference Room">
  <img src="assets/images/venue3.jpg" alt="Karuizawa Town">
</div>
```

### Adding a Banner/Hero Image

Add this at the top of [index.md](index.md) after the hero section:

```markdown
![Workshop Banner](assets/images/banner.jpg)
```

## Adding Logos

1. Add logo images to `assets/images/` (e.g., `logo-scitokyo.png`, `logo-jst.png`)

2. Replace the logo placeholders in [index.md](index.md) (around line 126-139):

```markdown
<div class="logo-container">
  <img src="assets/images/logo-scitokyo.png" alt="Institute of Science Tokyo" height="80">
  <img src="assets/images/logo-jst.png" alt="JST ASPIRE" height="80">
  <img src="assets/images/logo-partner.png" alt="Partner Institution" height="80">
</div>
```

## Customizing Colors

Edit [assets/css/style.scss](assets/css/style.scss) and modify the color variables (lines 9-16):

```scss
:root {
  --primary-blue: #1e5090;      /* Main blue color */
  --secondary-blue: #2874b5;    /* Secondary blue */
  --light-blue: #e8f1f8;        /* Light backgrounds */
  --accent-blue: #4a9fd8;       /* Links and accents */
  --dark-text: #2c3e50;         /* Text color */
  --light-gray: #f8f9fa;        /* Borders */
  --border-color: #d0e3f0;      /* Borders */
}
```

## Testing Locally

1. Install Jekyll:
   ```bash
   gem install jekyll bundler
   ```

2. Run the site locally:
   ```bash
   jekyll serve
   ```

3. View at `http://localhost:4000`

## Publishing to GitHub Pages

1. Commit your changes:
   ```bash
   git add .
   git commit -m "Update workshop website design"
   git push
   ```

2. Enable GitHub Pages in your repository settings:
   - Go to Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / (root)

3. Your site will be live at `https://[username].github.io/[repository-name]`

## Tips

- **Image Size:** Keep images under 500KB for faster loading
- **Logo Format:** PNG with transparent background works best
- **Responsive:** Images automatically adjust for mobile devices
- **Updates:** Edit [index.md](index.md) for content changes; [assets/css/style.scss](assets/css/style.scss) for styling

## Support

For questions or issues, contact:
- Erwin Wu: wu.e.aa@m.titech.ac.jp
