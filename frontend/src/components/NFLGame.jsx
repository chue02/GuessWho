// TODO: Consider renaming list-group

function NFLGame(){
    return(
        <>
        <h1>Guess the Athlete</h1>
        <ul className="list-group">
            <li className="list-group-item">Stats</li>
            <li className="list-group-item">Years active</li>
            <li className="list-group-item">Teams played</li>
            <li className="list-group-item">Draft selection</li>
            <li className="list-group-item">College(s)</li>
            <li className="list-group-item">Awards</li>
            <li className="list-group-item">Name</li>
        </ul>
        </>
    )
}

export default NFLGame