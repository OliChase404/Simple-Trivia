import './App.css';
import {React, useState, useEffect, createContext} from 'react'
import {Route, Routes, Navigate} from 'react-router-dom'
import Home from './Components/Home/Home';
import Navbar from './Components/Navbar/Navbar';

export const UserContext = createContext(null)

function App() {
  const [user, setUser] = useState(null)

  //add use effect for check session

  return (
    <div className="App">
      <UserContext.Provider value={{user, setUser}}>
        <Navbar />
        <Routes>
          <Route path='/' element={<Home />}/>
        </Routes>
      </UserContext.Provider>
    </div>
  );
}

export default App;
