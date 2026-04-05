import {Welcome} from './Welcome';
import {Hello} from './Hello';
import Button from './Button';
import {Card} from './Card';
import { UserProfile } from './UserProfile';
import { CandidateProfile } from './CandidateProfiles';
import { ContactForm } from './ContactFrom';
import { Products } from './Products';
import { Greetings } from './Greetings';
import { CardWrapper } from './CardWrapper';
import './App.css'
import React from "react";

function App() {

  return (
    <React.Fragment>

      <CardWrapper title="User Profile">

        <p>Bruce Wayne</p>
        <p>BatMan</p>
        <button>Edit Profile</button>
      </CardWrapper>

      <Greetings name="Ase Hossein" message="fuck you "/>
      <Greetings name="Dr.Ban" />
      <Greetings/>

      <h1>Hello World !</h1>

      <Products  
        title="Fuck Toy"
        price={12}
        inStock={false}
        categories={["Sex Toy", "Fuck Toy", "Adult"]}
      />
      <Welcome name="Bruce"/>
      <Welcome name="Diana"/>
      <Welcome name="Mario"/>
      <Hello />
      <Welcome />
      <Button/>
      <br />
      <CandidateProfile />
      <br />
      <button>Fuck You !</button>
      <Card />
      <UserProfile />
      <ContactForm />
   </React.Fragment>
  );
}

export default App
