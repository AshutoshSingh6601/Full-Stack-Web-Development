console.log("It's Working....");

let a = 10;
let b = 20.4539;
console.log (typeof(a.toString()));
console.log(b.toExponential(7));
console.log(b.toPrecision(3));
console.log(b.toFixed(2));
// console.log(parseInt("10"));
//It will only take integer value not take also after decimal value and also not take string
let c = (parseInt("10.45 kwdg"));      
console.log(c);
console.log(typeof(c));

let d = (parseFloat("10.45 kwdg"));       //It will only take integer value not take a string value
console.log(d);
console.log(typeof(d));