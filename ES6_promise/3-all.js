import {uploadPhoto, createUser} from './utils.js'

export default function handleProfileSignup() {
    return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
        // photo = { status: 200, body: 'photo-profile-1' }
        // user = { firstName: 'Guillaume', lastName: 'Salva' }
        console.log(`${photo.body} ${user.firstName} ${user.lastName}`)})
    .catch(() => console.log("Signup system offline"));
}