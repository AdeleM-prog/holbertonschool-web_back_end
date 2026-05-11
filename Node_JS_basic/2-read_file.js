const fs = require('fs');
module.exports = function countStudents(path) {

try {
  const data = fs.readFileSync(path, 'utf8');
  const lines = data.split('\n');
  const students = lines.slice(1).filter((line) => line.trim() !== '');

  Parser chaque ligne pour extraire firstname et field
  const result = Compter le total et grouper par champ
  console.log(`Number of students: ${result}`);
} catch (err) {
  throw new Error('Cannot load the database');
}
}