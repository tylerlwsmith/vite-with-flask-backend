import json
import os
from pathlib import Path

from flask import Blueprint

# Get environment variables.
VITE_SERVER_ORIGIN = os.getenv("VITE_SERVER_ORIGIN", "http://localhost:5173/assets")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Set application constants.
is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
is_production = ENVIRONMENT == "production" or is_gunicorn
project_path = Path(os.path.dirname(os.path.abspath(__file__)))

# Create assets blueprint that stores all Vite-related functionality.
assets_blueprint = Blueprint(
    "assets_blueprint",
    __name__,
    static_folder="assets_compiled/public",
    static_url_path="/assets/public",
)

# Load manifest file in production environment.
manifest = dict()
if is_production:
    manifest_path = project_path / "assets_compiled/manifest.json"
    try:
        with open(manifest_path, "r") as content:
            manifest = json.load(content)
    except OSError as exception:
        raise OSError(
            f"Manifest file not found at {manifest_path}. Run `npm run build`."
        ) from exception


# Add `asset()` function for producing Vite asset URLs.
@assets_blueprint.app_context_processor
def vite_urls():
    def dev(file_path):
        return f"{VITE_SERVER_ORIGIN}/{file_path}"

    def prod(file_path):
        try:
            return "/assets/" + manifest[file_path]["file"]
        except:
            return "asset-not-found"

    return dict(asset=prod if is_production else dev)


# Add `is_production` variable for determining the current environment.
@assets_blueprint.app_context_processor
def env():
    return dict(is_production=is_production)
