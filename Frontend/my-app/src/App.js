import React, { useState } from 'react';
import './App.css';

async function loginUser(username, password) {
  return fetch(`http://localhost:5000/login?username=${username}&password=${password}`, {
    method: 'POST',
  })
 }

function App() {
  const [username, setUsername] = useState();
  const [password, setPassword] = useState();

  const handleSubmit = async e => {
    e.preventDefault();
    await loginUser(username, password);
  }

  return(
    <div className="login-wrapper">
      <img src="/logo.jpg" alt="logo"></img>
      <div id='filetEntete'></div>
      <h1>Dossier des étudiants</h1>
      <form onSubmit={handleSubmit}>
        <label>
          <p>Code étudiant</p>
          <input type="text" onChange={e => setUsername(e.target.value)}/>
        </label>
        <label>
          <p>Mot de passe</p>
          <input type="password" onChange={e => setPassword(e.target.value)}/>
        </label>
        <div>
          <button type="submit">Connexion</button>
        </div>
      </form>
      <div id="filetPiedDePage"></div>
    </div>
  )
}

export default App;
