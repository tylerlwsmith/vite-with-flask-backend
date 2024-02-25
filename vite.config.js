import path from "node:path";

import { defineConfig } from "vite";

export default defineConfig({
  root: path.join(__dirname, "./assets_source"),
  base: "/assets/",
  build: {
    manifest: "manifest.json",
    outDir: path.join(__dirname, "./assets_compiled"),
    assetsDir: "bundled",
    emptyOutDir: true,
    copyPublicDir: true,
    rollupOptions: {
      input: ["assets_source/scripts/app.ts", "assets_source/styles/app.scss"],
    },
  },
});
