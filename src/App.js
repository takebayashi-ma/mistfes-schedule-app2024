import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import SchedulePage from './SchedulePage';

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/:date" element={<SchedulePage />} />
    </Routes>
  </Router>
);

export default App;
