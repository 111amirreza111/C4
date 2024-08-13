const express = require("express");
const fs = require("fs");
const path = require("path");
var cors = require("cors");
const { json } = require("body-parser");
const app = express();
const publicPath = path.join(__dirname, "Public");
// Define routes and middleware here
var message = "";
app.use(express.json());
app.use(
  cors({ origin: "http://127.0.0.1:8000", methods: "GET,POST,PUT,DELETE" })
);
app.use(express.static("public"));
app.get("/Home", (req, res) => {
  res.sendFile(`${publicPath}/Home.html`);
});

app.use(express.json());
const port = process.env.PORT || 3000; // Use environment variable for flexibility

app.post("/user_result_message", function (req, res) {
  if (req.body.result) {
    message = req.body.result;
  }

  res.send();
});
app.post("/user_result_message_sendclient", function (req, res) {
  //simple timeout
  setTimeout(() => {
    if (message == "") {
      res.send("");
    } else {
      res.send("" + message);
      message =""
    }
  }, 1000);
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
