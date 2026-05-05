export default function getListStudentIds(students) {
    if (Array.isArray(students) === false) {
        return [];
    }
    else {
        return students.map((student) => student.id);
    }
}