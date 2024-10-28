function allAllTypes(a, b){
	let answer = Number(a) + Number(b)
    return answer ? answer : "Oops! The output is invalid"
}

console.log(allAllTypes('55', 555))

let score = 85;
if (score >= 90) {
console.log("Grade: A");
} 
else if (score >= 80) {
console.log("Grade: B");
} 
else if (score >= 70) {
console.log("Grade: C");
} 
else {
console.log("Grade: F");
}