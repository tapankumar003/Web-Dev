const mysum1 = (x, y) => x + y;
console.log(mysum1(6,9))
const mysum2 = (x, y) => {x, y};
console.log(mysum2(55,7))
const mysum3 = (x, y) => ({x: x, y: y}); 
console.log(mysum3(4,6))
const mysum4 = (x, y) => {
  return {x: x, y: y};
}
console.log(mysum4(55,100))
const mysum5 = function(x, y) {
  return {x: x, y: y};
};
console.log(mysum5(2,1))
function mysum6(x, y) {
  return {x: x, y: y};
}
console.log(mysum6(1,1))