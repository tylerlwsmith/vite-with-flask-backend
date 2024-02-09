import json
import os
from pathlib import Path

from flask import Flask, render_template

# Get environment variables.
VITE_SERVER_ORIGIN = os.getenv("VITE_SERVER_ORIGIN", "http://localhost:5173/assets")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Set application constants.
is_production = ENVIRONMENT == "production"
project_path = Path(os.path.dirname(os.path.abspath(__file__)))

# Set up application.
app = Flask(
    __name__,
    static_url_path="",
    static_folder="public",
    template_folder="templates",
)

# Load manifest if running in production environment.
manifest = dict()
if is_production:
    manifest_path = project_path / "public/assets/manifest.json"
    try:
        with open(manifest_path, "r") as content:
            manifest = json.load(content)
    except OSError as exception:
        raise OSError(
            f"Manifest file not found at {manifest_path}. Run `npm run build`."
        ) from exception


# Add template function for locating Vite URLs.
@app.context_processor
def vite_urls():
    def dev(file_path):
        return f"{VITE_SERVER_ORIGIN}/{file_path}"

    def prod(file_path):
        try:
            return "/assets/{}".format(manifest[file_path]["file"])
        except:
            return "asset-not-found"

    return dict(asset=prod if is_production else dev)


# Add template variables.
@app.context_processor
def env():
    return dict(is_production=is_production)


# Setup application routes.
@app.get("/")
def homepage():
    return render_template("homepage.html")
