import path from "node:path";

import { defineConfig } from "vite";

export default defineConfig({
  root: path.join(__dirname, "./assets"),
//   base: "/assets/",
  build: {
    manifest: "manifest.json",
    ourDir: path.join(__dirname, "./public/assets"),
    rollupOptions: {
      input: "assets/scripts/app.ts",
    },
  },
});
