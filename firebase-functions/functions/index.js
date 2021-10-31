const functions = require("firebase-functions");


// test get request
exports.testGet = functions.https.onRequest((request, response) => {
  response.send("api is up");
});


// test post request
exports.testPost = functions.https.onRequest((request, response) => {
  response.send("hello: " + request.query.name);
});
