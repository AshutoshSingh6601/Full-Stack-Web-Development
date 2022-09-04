console.log("It's Workig......");

function sum(){
    let a = document.getElementById('wb').value;
    let b = document.getElementById('ai').value;
    let c = document.getElementById('ds').value;
    let d = document.getElementById('cc').value;

    let addition = parseInt(a)+parseInt(b)+parseInt(c)+parseInt(d);
        // console.log(addition);

        if (addition == 400) {
            document.getElementById('Percen').innerHTML="A+ Grade";
        } 
        else if (addition > 300) {
            document.getElementById('Percen').innerHTML="A Grade";
        }
        else if (addition > 200) {
            document.getElementById('Percen').innerHTML="B Grade";
        }
        else if (addition > 150) {
            document.getElementById('Percen').innerHTML="C Grade";
        }
        else {
            document.getElementById('Percen').innerHTML="D Grade";
        }
}
