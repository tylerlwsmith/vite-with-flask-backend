# Vite with Flask Backend

## Setup local

Install the npm dependencies.

```sh
npm install
```

Create a Python virtual environment then install the Pip dependencies.

```sh
python3 -m venv .venv
pip install -r requirements.txt
```

In one terminal window, start Vite in development mode.

```sh
npm run dev
```

In another terminal, start Flask in debug mode in order to have automatic app reloading.

```sh
flask --debug --app main run
```
