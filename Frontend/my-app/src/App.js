import React, { useState } from 'react';
import './App.css';
import { Link, Navigate } from 'react-router-dom';

async function loginUser(username, password) {
  return await fetch(`http://10.200.7.14:5000/login?username=${username}&password=${password}`, {
    method: 'POST',
  })
  .then(response => response.json())
}

function App() {
  const [username, setUsername] = useState();
  const [password, setPassword] = useState();

  const [state, setState] = useState(undefined);
  const [isError, setError] = useState(false);

  const handleSubmit = async e => {
    e.preventDefault();
    let result = await loginUser(username, password).catch(e => undefined);
    setState(result);
    setError(result === undefined);
  }

  return(
    <div className="login-wrapper">
      {state !== undefined && (<Navigate to="/options" state={{ state: state }} replace={true}/>)}

      <img src="/logo.jpg" alt="logo"></img>
      <div id='filetEntete'></div>
      <h1>Dossier des étudiants</h1>
      <form onSubmit={handleSubmit}>
        {isError && (<label style={{color: "red"}}>Erreur de connexion</label>)}
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
