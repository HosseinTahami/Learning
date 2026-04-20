export const NameList = () => {

    const names = ["Hossein", "Bruce", "AmirArsalan", "Maria"];

    const nameList = names.map((name, index) => <h2 key={index}>{name}</h2>);


    return (
        <div>
            {nameList}
        </div>
    );
}