import React from "react";
import ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import App from "./App";
import { Brand } from "./components";
import Connector from "./containers/dashboard/Connector";
import Dashboard from "./containers/dashboard/Dashboard";
import ConnectorB from "./containers/dashboardB/ConnectorB";
import Signin from "./containers/signin/Signin";
import Signup from "./containers/signup/Signup";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
  {
    path: '/signin',
    element : <Signin/>,
  },
  {
    path: '/signup',
    element: <Signup/>,
  },
  {
    path: '/dashboard',
    element: <Connector/>,
  },
  {
    path: '/dashboardB',
    element: <ConnectorB/>,
  }

]);


ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);