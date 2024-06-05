import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import SchedulePage from './SchedulePage';
import HomePage from './HomePage';

const App = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/6-8" element={<SchedulePage date="6/8" />} />
          <Route path="/6-9" element={<SchedulePage date="6/9" />} />
          <Route path="/" element={<HomePage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
