console.log(`Console Working....`);


function sum(){
let webdev = document.getElementById('wb').value;
let AI = document.getElementById('ai').value;
let datasci = document.getElementById('ds').value;
let cloudcom = document.getElementById('cc').value;
    // Addition
    let add= parseFloat(webdev) + parseFloat(AI) + parseFloat(datasci) + parseFloat(cloudcom);
    console.log(add);
    // Percentage
    let per = (add/400)*100;
    console.log(per);
    // Printing the value
    document.getElementById('Percen').innerHTML=`The Addition is ${add}, <br> Percentage is ${per}`;
    
}  