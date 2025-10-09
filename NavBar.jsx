import React from "react";
import styles from "./NavBar.module.css"
import { Link } from "react-router-dom"; 

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">MySite</div>
      <ul className={styles}>
         <li><link to="/">HOME</link></li>
         <li><link to="/movies">MOVIES</link></li>
         <li><link to="/register">REGISTER</link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
