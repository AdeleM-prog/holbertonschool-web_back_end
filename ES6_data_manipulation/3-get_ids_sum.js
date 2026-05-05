export default function getStudentIdsSum(students){
    if (Array.isArray(students) === false) {
        return [];
    }
    else {
        return students.reduce((acc, student) => acc + student.id, 0);
    }
}