export default function handleResponseFromAPI(promise){
    return promise.then(resolve => {
        return {status: 200, body: 'success'};
    }).catch(reject => {
        return new Error();
    }).finally(() => console.log("Got a response from the API"))
}