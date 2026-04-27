// import FuckYou from './FuckYou';
import { FuckYou } from './FuckYou';
import { StyledForm } from './StyledForm';
import { UserProfile } from './UserProfile';
import Button from './Button';
import {Hello, HellWithoutJSX} from "./Hello"
import { ContactForm } from './ContactForm';
import { CandidateProfile } from './CandidateProfile'
import { Product } from './Product';
import { Fucking } from './Fucking'
import { CardWrapper } from './CardWrapper'
import './App.css'
import { ProductList } from './ProductList';
import { NameList } from './NameList';
import { Alert } from './Alert';

function App() {

  return (

    <div>



      <Alert>
        Something went Wrong
      </Alert>

      <Alert type='error'>
        Something went Wrong
      </Alert>

      <Alert type='success'>
        Good
      </Alert>
      <hr />
      <NameList />

      <ProductList />
      <hr />

      <CardWrapper title="User Profile">
        <p>Bruce Wayne</p>
        <p>Batman</p>
      </CardWrapper>

      <hr />


      <FuckYou />
      <hr />
      <FuckYou name="Hossein" alias="Polito Student"/>
      <hr />
      <UserProfile></UserProfile>
      <hr />
      <Product 
        title="Toy"
        price={233.56}
        inStock={true}
        categories={["Electronics", "Computer", "Gaming"]}
      />
      <hr />
      <h1>Fuck:</h1>
      <hr />
      <FuckYou />
      <hr />
      <Button />
      <hr />
      <HellWithoutJSX />
      <hr />
      <Hello />
      <hr />
      <ContactForm></ContactForm>
      <hr />
      <StyledForm></StyledForm>
      <hr />
      <CandidateProfile/>
      <hr />
      <div>
        <Fucking />
        <Fucking name="Sara" message="Fuck you and beyond."/>
      </div>
      <hr />
    </div>
    

  );
}

export default App
