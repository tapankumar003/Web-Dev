let person = {name: 'Tapan', age: 26}

let {name, age} = person

console.log(`name: ${name} age: ${age}`)


function hello({name, age}){
    console.log(`name: ${name} age: ${age}`)
}
hello(person);