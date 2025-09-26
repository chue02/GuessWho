// TODO: Move the random error message logic to a component

const NotFound = () => {
    // List of flavor error messages
    const errors = [
        "Indexing E credited to the developer",
        "Index out of bounds, 10 yard penalty for the developer",
        "Technical foul on the developer, bad page accessed",
        "Accessing bad page, E credited to user",
        "Out of bounds page, 5 yard penalty for the user, repeat first down",
        "Technical foul on the user, attempting to access bad page",
        "Bad page accessed, user has been ejected from the game"
    ];

    // Indexes error pages then select a random index 
    const randomIndex = Math.floor(Math.random() * errors.length);
    const errorMessage = errors[randomIndex];

    return (
        <div>
            <h1>404 Error</h1>
            <h3>{errorMessage}</h3>
        </div>
    );
};

export default NotFound