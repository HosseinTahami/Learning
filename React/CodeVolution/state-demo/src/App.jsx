import './App.css'
import { Counter } from './Counter';
import { LoginCard } from './LoginCard';
import { UserDashboard } from './UserDashboard';
import { SimpleCounter } from './SimpleCounter';

function App() {
  return (
    <div>
      <h1>Hossein Tahami</h1>
      <hr />
      <Counter />
      <br />
      <LoginCard />
      <UserDashboard isPremium={true}/>
      <br />
      <SimpleCounter />
    </div>
  )
}

export default App;
