# Vite with Flask Backend

This repository is a minimal but complete proof-of-concept for a Vite with a backend Flask integration. It is loosely inspired by Laravel's asset bundling, but provides a much lighter abstraction between Vite and the Flask backend.

This demo supports **TypeScript** and **Scss**, but other file formats like **JSX** could be added.

## How to use Vite assets in this demo

To add an input asset (equivalent to a Webpack entrypoint), first add it to the `build.rollupOptions.input` array in `vite.config.js`. The asset must live in the `assets/` directory.

```js
// Truncated vite.config.js file

export default defineConfig({
  build: {
    rollupOptions: {
      input: ["assets/scripts/app.ts"],
    },
  },
  // more configuration...
});
```

To use the asset in Flask, use the `asset()` helper in the Jinja2 html templates, passing it the path of the asset within the `assets` directory.

```html
<script type="module" src="{{ asset('scripts/app.ts') }}"></script>
```

Any assets imported by `app.ts` will automatically be included by Vite.

## Setting up the local development environment

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

## Running the app in development mode

In one terminal window, start Vite in development mode.

```sh
npm run dev
```

In another terminal, start Flask in `debug` mode, which provides automatic app reloading while developing.

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

## Potential gotchas

When running in development, Vite will process & serve any file within the `assets` directory whether-or-not it is an input asset included in the `build.rollupOptions.input` array in `vite.config.js`. You must ensure that any asset that is referenced in a Jinja template is also included in the input asset array prior to building the production assets.

When running this demo using production settings, the `manifest.json` that lists all of the compiled assets is publicly viewable at http://127.0.0.1:8000/assets/manifest.json. If you want to learn how to keep the build manifest private, [view my blog post](https://dev.to/tylerlwsmith/move-manifestjson-to-outdirs-parent-directory-in-vite-5-5fpf) that details multiple ways to move it out of the public directory.

## TODO

Things I'd still like to do before calling this repo complete:

- Use image from scss file to make sure it loads in development and production
- Check import aliases from `playground` with Scss and JS
- Bonus: hot reloading for templates (maybe? https://vitejs.dev/guide/build.html#rebuild-on-files-changes)
- Add favicon
