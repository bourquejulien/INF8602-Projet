import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import './index.css';
import App from './App';
import Options from './Options';

const root = ReactDOM.createRoot(document.getElementById('root'));

const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
  {
    path: "/options",
    element: <Options/>,
  },
]);

function Root() {
  return <RouterProvider router={router} />
}

root.render(
  <React.StrictMode>
      <Root/>
  </React.StrictMode>
);
