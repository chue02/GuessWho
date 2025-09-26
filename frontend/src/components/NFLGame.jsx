// TODO: Consider renaming list-group

let DummyAthlete = ["30,000 passing yards, 144 passing TDs, 3 recs, 10 rec yards, 1 rec TD", "2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018",
    "OAK, LVR, NYJ", "2010 round 1 pick 33", "UCLA", "Pro Bowl x2", "Fake QB"
]

let ShowYears = true
let ShowTeams = true
let ShowDraft = true
let ShowSchool = true
let ShowAwards = true
let ShowName = false

const DontShow = "HIDDEN"

// TODO: Figure out how to filter stats based on position (e.g. QB only display passing stats, WR only display rec stats, etc.)
// TODO: Figure out how to display teams based on abbreviations (e.g. OAK and LVR are Raiders)
function NFLGame(){
    return(
        <>
        <h1>Guess the Athlete</h1>
        <ul className="list-group">
            <li className="list-group-item">{DummyAthlete[0]}</li>
            <li className="list-group-item">{ShowYears ? DummyAthlete[1]: DontShow}</li>
            <li className="list-group-item">{ShowTeams ? DummyAthlete[2]: DontShow}</li>
            <li className="list-group-item">{ShowDraft ? DummyAthlete[3]: DontShow}</li>
            <li className="list-group-item">{ShowSchool ? DummyAthlete[4]: DontShow}</li>
            <li className="list-group-item">{ShowAwards ? DummyAthlete[5]: DontShow}</li>
            <li className="list-group-item">{ShowName ? DummyAthlete[6]: DontShow}</li>
        </ul>
        </>
    )
}

export default NFLGame