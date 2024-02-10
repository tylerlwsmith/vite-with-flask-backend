const message: string = "Hello, world!";

console.log(message);

if (import.meta.hot) {
  import.meta.hot.accept();
}
