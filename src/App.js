import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './Home';
import SchedulePage from './SchedulePage';
import './App.css';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/6-8" element={<SchedulePage date="6/8" />} />
        <Route path="/6-9" element={<SchedulePage date="6/9" />} />
      </Routes>
    </div>
  );
}

export default App;
