export const Welcome = (props) => {
  console.log(props);
  console.log("Fuck you");
  return (
    <>
      <h2> Welcome, {props["name"]} !</h2>
    </>
  );
}

