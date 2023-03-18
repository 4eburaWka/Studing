const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  // Чтение файла index.html
  fs.readFile('index.html', (err, data) => {
    if (err) {
      // Если произошла ошибка чтения файла, отправляем код ошибки 500
      res.writeHead(500, {'Content-Type': 'text/plain'});
      res.end('Error loading index.html');
    } else {
      // Отправляем содержимое файла как ответ на запрос
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.end(data);
    }
  });
});

server.listen(8080, () => {
  console.log('Server running at http://localhost:8080/');
});
