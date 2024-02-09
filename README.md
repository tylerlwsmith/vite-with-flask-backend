# Vite with Flask Backend

## Setup local

Install the npm dependencies.

```sh
npm install
```

Create a Python virtual environment then install the Pip dependencies.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

In one terminal window, start Vite in development mode.

```sh
npm run dev
```

In another terminal, start Flask in debug mode in order to have automatic app reloading.

```sh
flask --debug --app main run --port 8000
```

For more Flask CLI arguments, [check this post](https://geekpython.medium.com/how-to-run-flask-app-from-the-command-line-in-windows-4b9865059a9c).

## Running with production assets

First, build the production assets:

```sh
npm run build
```

Then boot the production server with the following command:

```sh
gunicorn -w 4 -b :8000 'main:app'
```
