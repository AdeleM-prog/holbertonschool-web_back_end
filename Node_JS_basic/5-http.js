const http = require('http');
const fs = require('fs');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!\n');
  } else if (req.url === '/students') {
    const filePath = process.argv[2];
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        res.end('Cannot load the database');
        return;
      }
      let response = 'This is the list of our students\n';

      const splitlines = data.split('\n');
      const slicedata = splitlines.slice(1).filter((splitline) => splitline.trim() !== '');
      response += `Number of students: ${slicedata.length}\n`;

      const students = {};
      slicedata.forEach((splitline) => {
      const columns = splitline.split(',');
      const firstname = columns[0];
      const field = columns[3];
      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstname);
      });

      Object.keys(students).forEach((field) => {
      response += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
      });

      res.end(response);
    })
    });
    }
app.listen(1245);
module.exports = app;
