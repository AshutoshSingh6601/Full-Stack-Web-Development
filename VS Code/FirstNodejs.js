// console.log("Hello world");

const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.end(`<!DOCTYPE html>
  <html lang="en">
  
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Form</title>
      <style>
           body div{
       text-align: center;
       background-color: chartreuse;
       text-align: center;
       margin: 30px 497px;
       border-radius: 8px;
       border: 2px solid black;
       padding: 10px 0px;
       
   }
   body h1{
       color: chartreuse;
       background-color: blue;
       text-align: center; 
       border: 2px solid brown;
       border-radius: 8px;
       margin: 0px 100px;
       margin-bottom: 15px;
   }
   #btn{ 
       text-align: center;
       margin: 20px 50px;
       padding: 5px 10px;
   }
      </style>
      
  </head>
  
  <body>
      <div>
          <h1>Form</h1>
          Name: <input type="text" name="ashutosh">
          <br><br>
          Role: <input type="text">
          <br><br>
          Email: <input type="email" onclick="emailvalidation()" name="a">
          <br><br>
          Date Of Birth: <input type="date" name="" id="">
          <br><br>
          Bonus: <input type="number">
          <br><br>
          Are you eligible: <input type="checkbox" name="" id="">
          <br><br>
          Gender: Male <input type="radio" name="as"> Female <input type="radio" name="as"><br>
          <!-- Write <textarea name="" id="" cols="30" rows="10"></textarea> -->
          <input type="button" value="button" onclick="emailvalidation()" id="btn">
          <input type="reset" value="Reset" name="ashutosh" id="btn">
  
      </div>
  
      
  </body>
  
  </html>`);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});