// const FuckYou = () => {

//   return <h2>Fuck You, Who Every the fuck you are.</h2>;

// };

// export default FuckYou;


export const FuckYou = (props) => {

  return <h2>Fuck { props.name ? props.name : "You" } a.k.a {props.alias ? props.alias : "No-One"}!</h2>;

};


// When using export 
// import {FuckYou} from "./FuckYou.jsx" 


// when using export default FuckYou
// import FuckYou from "./FuckYou.jsx"