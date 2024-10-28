let [name, ...rest] = ["Tom", 10, "Seoul"];
console.log(name)
console.log(rest)

let names = ["Steve", "John"];
let students = ["Tom", ...names, ...names];
console.log(students)

let tom = {
    name: "Tom",
    age: 10,
    region: "Seoul",
  };
  
  let steve = {
    ...tom,
    name: "Steve",
  };
  console.log(steve)