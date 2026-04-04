import {Welcome} from './Welcome';
import {Hello} from './Hello';
import Button from './Button';
import {Card} from './Card';
import { UserProfile } from './UserProfile';
import { ContactForm } from './ContactFrom';
import './App.css'
import React from "react";

function App() {

  return (
    <React.Fragment>
      <h1>Hello World !</h1>
      <Hello />
      <Welcome />
      <Button/>
      <br />
      <button>Fuck You !</button>
      <Card />
      <UserProfile />
      <ContactForm />
   </React.Fragment>
  );
}

export default App
