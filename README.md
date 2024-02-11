# Vite with Flask Backend

This repository is a minimal but complete proof-of-concept for a Vite with a backend Flask integration. It is loosely inspired by Laravel's asset bundling, but provides a much lighter abstraction between Vite and the Flask backend. The techniques used in this project could be adapted to integrate Vite with other backends like Go, Django, Ruby, and others.

This demo supports **TypeScript** and **Scss**, but other file formats like JSX could be added.

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

To use the asset in Flask, use the `asset()` helper in the Jinja2 html templates, passing it the path of the asset within the `assets/` directory.

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
gunicorn --workers 4 --bind 127.0.0.1:8000 'main:app'
```

## Potential gotchas

### Assets may be accidentally omitted in production

Vite's development server will build & serve all requested files within the `assets/` directory, even if they are not included in the `build.rollupOptions.input` array in `vite.config.js`. If input files are not included as input assets in Vite's config file, they won't get built when running `npm run build`, and therefore won't be available in production.

Ensure that any asset that is referenced in a template is also included in Vite's input asset array in prior to building the production assets.

### The manifest file is publicly viewable in production

When running this demo using production settings, the `manifest.json` that lists all of the compiled assets is publicly viewable at http://127.0.0.1:8000/assets/manifest.json. If you want to learn how to keep the build manifest private, [view my blog post](https://dev.to/tylerlwsmith/move-manifestjson-to-outdirs-parent-directory-in-vite-5-5fpf) that details multiple ways to move it out of the public directory.

### The JS entrypoints don't need a modulepreload polyfill

Vite's [Backend Integration Guide](https://vitejs.dev/guide/backend-integration.html) mentions adding `import 'vite/modulepreload-polyfill'` to the top of JS entrypoints if `build.polyfillModulePreload` is not disabled. We do not need to do this because our templates don't implement [module preload links](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/modulepreload).
