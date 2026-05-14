import readDatabase from "../utils";

class StudentsController {
  static getAllStudents(req, res) {

    const database = process.argv[2];
    readDatabase(database)

    .then((students) => {
      let response = 'This is the list of our students\n';

    Object.keys(students)
    .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
    .forEach((field) => {
      response += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
    });

    res.status(200).send(response);
    })
    .catch(() => {
      res.status(500).send('Cannot load the database');
    });
  }

  static getAllStudentsByMajor(req, res) {
    const major = req.params.major;

    if (major !== 'CS' && major !== 'SWE') {
    res.status(500).send('Major parameter must be CS or SWE');
    return;
    }

    const database = process.argv[2];
    readDatabase(database)

    .then((students) => {
      res.status(200).send(`List: ${students[major].join(', ')}`);
    })

    .catch(() => {
      res.status(500).send('Cannot load the database');
    });
  }
}
export default StudentsController;
