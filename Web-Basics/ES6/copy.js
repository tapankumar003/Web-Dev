const obj1 = { value1: 10 };
const obj2 = obj1; // Shallow copying
const obj3 = JSON.parse(JSON.stringify(obj1)) // deep copy

obj1.value1 += 1;

// guess the result! Let's try it together
console.log(`obj1:`, obj1);
console.log(`obj2:`, obj2);
console.log(`obj3:`, obj3);



