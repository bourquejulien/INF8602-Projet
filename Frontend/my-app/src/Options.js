import React, { useState } from 'react';
import './Options.css';
import { useLocation } from 'react-router-dom';

function Options() {
  const location = useLocation();
  const state = location.state.state

  return(
    <div>
      <div className="options-select">
        <img src="/logo.jpg" alt="logo"></img>
        <div className='info'>
          <div id='filetEntete'></div>
          {state !== undefined && ( <label>{state.first_name} {state.last_name} - </label>)}
          {state !== undefined && ( <label>{state.username} - {state.email}</label>)}
        </div>
        <h1>Dossier des étudiants</h1>
        <div id="filetPiedDePage"></div>
      </div>
      <div className="button-select">
        <button>Renseignements personnels</button>
        <button>Conflits d'horaire</button>
        <button>Choix de cours</button>
        <button>Bulletin</button>
        <button>Dossier financier</button>
      </div>
    </div>
  )
}

export default Options;
