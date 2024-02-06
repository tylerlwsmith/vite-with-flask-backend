import os
from flask import Flask, render_template

# Get environment variables.
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
is_production = ENVIRONMENT == "production"

# Set up application.
app = Flask(
    __name__,
    static_url_path='',
    static_folder='public',
    template_folder='templates'
)

# Add template function for locating Vite URLs.
@app.context_processor
def vite_urls():
    manifest = None
    vite_origin = "http://localhost:5173/assets"
    if is_production:
        manifest = None # todo

    def development_url(file_path):
        return f"{vite_origin}/{file_path}"
    
    def production_url(file_path):
        pass

    return dict(asset=production_url if is_production else development_url)

@app.context_processor
def env():
    return dict(is_production=is_production)

# Setup application routes.
@app.get('/')
def homepage():
    return render_template("homepage.html")
