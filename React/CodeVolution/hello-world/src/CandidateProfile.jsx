export const CandidateProfile = () => {

    const name = "Peter Parker"
    const role = "Web Developer"
    const yearOfExperience = 49;
    const isAvailabel = true;
    return (
        <>
            <h2>{name}</h2>
            <p>{role}, Spider-man {yearOfExperience} fucking years.</p>
            <p>Status: {isAvailabel ? "Available for hire" : "Not Available"}</p>
            <p>Contact: {name.toLowerCase().replace(" ", ".")}@email.com</p>
        </>
    );
};