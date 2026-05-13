const fs = require('fs');

function countStudents(path){
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf-8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the databse'));
                return;
            } else {
                const lines = data.split('\n');
                
                const students = lines
                .slice(1)
                .filter((line) => line.trim() !== '')
                .map((line) => {
                    const values = line.split(',');
                    return {firstname: values[0], field: values[3]};
                });
                
                const groups = {};
                
                students.forEach((student) => {
                    if (groups[student.field] === undefined){
                    groups[student.field] = [];
                    }
                    groups[student.field].push(student.firstname);
                })
                console.log(`Number of students: ${students.length}`);
                
                Object.keys(groups).forEach((field) => {
                    console.log(`Number of students in ${field}: ${groups[field].length}. List: ${groups[field].join(', ')}`)
                });
            resolve();
            };
        })
    });
}
module.exports = countStudents;
