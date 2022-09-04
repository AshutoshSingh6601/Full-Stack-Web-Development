console.log(`It's working.......`)

const developer = {
    front:"html",
    back:"Python",
    fullstack:"both",
    frontend:{
        body:"html",
        brain:"javascript",
        skin:"css",
    }
}

console.log(developer.front);

console.log(developer.frontend.brain);
// added proparties:value in developer(object)
let d = developer.backend="django";
console.log(developer);

delete developer.fullstack;
// it will gives you undefined becouse you will deleted this 
console.log(developer["fullstack"]);

console.log(developer["back"]);