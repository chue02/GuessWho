import react from 'react'
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
import NFL from "./pages/NFL"

function nflGame(){
  return <Navigate to="/NFL" />
}

// TODO: For now, create a page for each league (e.g. <Route path="/NFL" element = {<NFL />} />) 
// Can consolidate the game pages into the Home page or one big game page later

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path = "/" element = {<Home />} />
        <Route path="/NFL" element = {<NFL />} /> 
        <Route path="*" element = {<NotFound />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
