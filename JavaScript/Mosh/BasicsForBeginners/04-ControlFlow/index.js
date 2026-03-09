
// if - else Statements

let hour = 8;

if ( 6 <= hour && hour < 12){
    console.log("Good Morning !");
} else if ( 12 <= hour && hour < 18) {
    console.log("Good Afternoon !");
} else {
    console.log("Good Evening !");
}


// Switch Case

let role;

switch(role) {

    case 'guest':
        console.log('Guest User');
        break;
    
    case 'moderator':
        console.log('Moderator User');
        break;
    
    default:
        console.log('Unknown User');

}