// TODO: For now, create a page for each league, can consolidate the game pages into the Home page or one big game page later

// TODO: should be '../components/NFLGame', but because I originally named file nflGame.jsx, React wants me to import it OG casing. Why?
import NFLGame from '../components/nflGame' 

function NFL(){
    return <div><NFLGame /></div>
}

export default NFL