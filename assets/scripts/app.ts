import { setupCounter } from "./counter.ts";

document.addEventListener("DOMContentLoaded", function () {
  const counter = document.querySelector<HTMLButtonElement>("#counter");
  if (!counter) return;

  setupCounter(counter);
});
