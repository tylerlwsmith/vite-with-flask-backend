import path from "node:path";

import { defineConfig } from "vite";

export default defineConfig({
  root: path.join(__dirname, "./assets"),
  base: "/assets/",
  build: {
    manifest: "manifest.json",
    outDir: path.join(__dirname, "./public/assets"),
    assetsDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      input: ["assets/scripts/app.ts", "assets/styles/app.scss"],
    },
  },
});
