from flask import Flask, render_template
from vite_blueprint import vite_blueprint


# Set up application.
app = Flask(
    __name__,
    static_url_path="/",
    static_folder="public",
    template_folder="templates",
)

# Provide Vite context processors and static assets directory.
app.register_blueprint(vite_blueprint)


# Setup application routes.
@app.get("/")
def homepage():
    return render_template("homepage.html")


# Start the app if the file is run directly.
if __name__ == "__main__":
    app.run()
