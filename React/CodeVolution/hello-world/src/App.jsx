// import FuckYou from './FuckYou';
import { FuckYou } from './FuckYou';
import { StyledForm } from './StyledForm';
import { UserProfile } from './UserProfile';
import Button from './Button';
import {Hello, HellWithoutJSX} from "./Hello"
import { ContactForm } from './ContactForm';
import { CandidateProfile } from './CandidateProfile'
import './App.css'



function App() {

  return (

    <div>
      <UserProfile></UserProfile>
      
      <h1>Fuck:</h1>
      <FuckYou />
      <Button />
      <br></br>
      <Button />
      <HellWithoutJSX />
      <Hello />
      <ContactForm></ContactForm>
      <StyledForm></StyledForm>
      <CandidateProfile/>
    </div>
    

  );
}

export default App
