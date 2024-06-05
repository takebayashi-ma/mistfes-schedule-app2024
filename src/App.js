import React from 'react';
import { Route, Routes } from 'react-router-dom';
import HomePage from './HomePage';
import SchedulePage from './SchedulePage';
import './App.css';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/6-8" element={<SchedulePage date="6/8" />} />
        <Route path="/6-9" element={<SchedulePage date="6/9" />} />
      </Routes>
    </div>
  );
}

export default App;
