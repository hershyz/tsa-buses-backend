<h1>TSA Buses Backend</h1>

<p>
    This repository contains the Node.js + Firebase API source for the 2021-2022 TSA Software Development project.
</p>

<ul>
    <li><a href="https://github.com/hershyz/tsa-buses-backend/tree/main/firebase-functions">Cloud Functions</a></li>
    <li><a href="https://github.com/hershyz/tsa-buses-backend/tree/main/endpoint-tests">Endpoint Tests</a></li>
</ul>

<h4>Firebase CLI tools setup</h4>
<pre>
    > npm install -g firebase-tools
    > firebase login
</pre>

<h4>Clone the repository, install Node dependencies, and deploy cloud functions to Firebase:</h4>
<pre>
    > git clone https://github.com/hershyz/tsa-buses-backend.git
    > cd tsa-buses-backend/firebase-functions
    > npm install
    > firebase deploy --only functions
</pre>