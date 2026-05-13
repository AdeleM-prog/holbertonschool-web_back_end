const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n');

    const students = lines
      .slice(1)
      .filter((line) => line.trim() !== '')
      .map((line) => {
        const values = line.split(',');
        return { firstname: values[0], field: values[3] };
      });

    const groups = {};

    students.forEach((student) => {
      if (groups[student.field] === undefined) {
        groups[student.field] = [];
      }
      groups[student.field].push(student.firstname);
    });
    console.log(`Number of students: ${students.length}`);

    Object.keys(groups).forEach((field) => {
      console.log(`Number of students in ${field}: ${groups[field].length}. List: ${groups[field].join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};
