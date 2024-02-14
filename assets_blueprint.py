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


# Add `is_production` variable and `asset()` function to app context.
@assets_blueprint.app_context_processor
def add_context():
    def dev_asset(file_path):
        return f"{VITE_SERVER_ORIGIN}/{file_path}"

    def prod_asset(file_path):
        try:
            return "/assets/" + manifest[file_path]["file"]
        except:
            return "asset-not-found"

    return {
        "asset": prod_asset if is_production else dev_asset,
        "is_production": is_production,
    }
