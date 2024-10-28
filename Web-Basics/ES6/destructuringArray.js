// Just like the case with objects, arrays are also subject to deconstructive allocation!

const testArr = [1, 2, 3, 4, 5];
const [val1, val2, val3, val4, val5] = testArr;

console.log(val1);

// Additional example

let [name] = ["Tom", 10, "Seoul"];
let [, age] = ["Tom", 10, "Seoul"];
console.log(age)
// let [name, age, region] = ["Tom", 10, "Seoul"];
// let [name, age, region, height] = ["Tom", 10, "Seoul"];
// let [name, age, region, height = 150] = ["Tom", 10, "Seoul"];