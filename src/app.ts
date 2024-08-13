import axios from "../node_modules/axios/index";
var axois = require("axios");

const form = document.querySelector("form");
const nameInput = <HTMLInputElement>document.getElementById("login__username");
const passwordInput = <HTMLInputElement>(
  document.getElementById("login__password")
);

form.addEventListener("submit", (event) => {
  event.preventDefault(); // Prevent default form submission
  eraseCookie('token')
  axios
  .post("http://127.0.0.1:8000/login", {
    userName: nameInput.value,
    password: passwordInput.value,
  })
  .then((response) => {
    console.log(JSON.parse(response.data))
    if(JSON.parse(response.data).submit)
    {
      setFloatCookie("token" ,JSON.parse(response.data).token ,1)
      window.location.pathname += "Home";
     
    }else{
      return 
    }
  
   })
  .catch((error) => {
    console.log("axios error", error);
  });
  
});


function setFloatCookie(name, value, days) {
  let expires = "";
  if (days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || 0) + expires + "; path=/";
}


function getFloatCookie(name) {
  const nameEQ = name + "=";
  const ca = document.cookie.split(';');
  for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) return parseFloat(c.substring(nameEQ.length, c.length));
  }
  return null;
}

function eraseCookie(name) {
  document.cookie = name + '=; Max-Age=-99999999;';
}




