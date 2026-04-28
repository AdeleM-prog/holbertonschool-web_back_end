export default function appendToEachArrayValue(array, appendString) {
  const newArray = [...array];
  for (const [index, value] of newArray.entries()) {
    newArray[index] = appendString + value;
  }

  return newArray;
}
