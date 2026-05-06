export default function updateUniqueItems(map) {
    if (map instanceof Map !== true) {
        throw new Error('Cannot process')
    } else {
    for (const [key, value] of map){
        if (value === 1){
        map.set(key, 100);
    }
    }
    return map;
}
}