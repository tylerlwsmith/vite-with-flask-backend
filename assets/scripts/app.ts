// add the beginning of your app entry
import "vite/modulepreload-polyfill";

const message: string = "Hello, world!";

console.log(message);

if (import.meta.hot) {
  import.meta.hot.accept();
}
