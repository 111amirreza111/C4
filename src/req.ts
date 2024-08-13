import axios from "../node_modules/axios/index";

const form = document.querySelector("form");
var A = <HTMLInputElement>document.getElementById("dropdown_A");
var B = <HTMLInputElement>document.getElementById("dropdown_B");
var C = <HTMLInputElement>document.getElementById("dropdown_C");
var D = <HTMLInputElement>document.getElementById("dropdown_D");

form.addEventListener("submit", (event) => {
  event.preventDefault(); // Prevent default form submission
  //  window.alert("" + A.value+B.value+C.value+D.value);

  axios
    .post("http://127.0.0.1:8000/submit-request", {
      token: getFloatCookie("token"),
      A: parseInt(A.value),
      B: parseInt(B.value),
      C: parseInt(C.value),
      D: parseInt(D.value),
    })
    .then(async (response) => {
      if (JSON.parse(response.data).submit) {
        await axios
          .post("http://localhost:3000/user_result_message_sendclient")
          .then((response) => {
            if (response.data == "") {
              window.alert("timeout...")
            }else{
              window.alert(response.data)
            }
          });
      } else {
        window.location.replace("http://localhost:3000");
      }

      if (JSON.parse(response.data).serverproblem) {
        window.alert("Server is busy...");
      }
    })
    .catch((error) => {
      console.log("axios error", error);
      window.alert("Server is busy...");
    });
});

function setFloatCookie(name, value, days) {
  let expires = "";
  if (days) {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || 0) + expires + "; path=/";
}

function getFloatCookie(name) {
  const nameEQ = name + "=";
  const ca = document.cookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) === " ") c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) === 0)
      return parseFloat(c.substring(nameEQ.length, c.length));
  }
  return null;
}

function eraseCookie(name) {
  document.cookie = name + "=; Max-Age=-99999999;";
}
