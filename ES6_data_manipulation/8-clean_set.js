export default function cleanSet(set, startString) {
    if (typeof startString !== 'string' || startString === ''){
        return '';
    }
    const result = new Array;
    set.forEach((element) => {
            if (element.startsWith(startString) === true) {
            const slicedElement = element.slice(startString.length);
            result.push(slicedElement);
        }
    });
    return result.join('-');
    }