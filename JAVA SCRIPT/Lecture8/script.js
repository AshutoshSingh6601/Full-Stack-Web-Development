console.log("It's Working....");

function OTP(){
    let printOtp = document.getElementById("demo").innerHTML = Math.floor(Math.random() * (9999 - 1000)) + 1000 ;
    alert(printOtp);
}