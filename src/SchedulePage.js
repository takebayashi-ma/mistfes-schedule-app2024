import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import './App.css';
import data6_8 from './data6_8.json';
import data6_9 from './data6_9.json';

const SchedulePage = () => {
  const { date } = useParams();
  const [selectedSchedules, setSelectedSchedules] = useState([]);
  const [menuOpen, setMenuOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (date) {
      const storedSchedules = JSON.parse(localStorage.getItem(`selectedSchedules_${date}`)) || [];
      setSelectedSchedules(storedSchedules);
    }
  }, [date]);

  const handleToggleSchedule = (scheduleId) => {
    let updatedSchedules;
    if (selectedSchedules.includes(scheduleId)) {
      updatedSchedules = selectedSchedules.filter(id => id !== scheduleId);
    } else {
      updatedSchedules = [...selectedSchedules, scheduleId];
    }

    setSelectedSchedules(updatedSchedules);
    if (date) {
      localStorage.setItem(`selectedSchedules_${date}`, JSON.stringify(updatedSchedules));
    }
  };

  const getSchedules = () => {
    const schedules = date === '6-8' ? data6_8 : data6_9;
    return schedules.sort((a, b) => a.artist.localeCompare(b.artist));
  };

  const getSortedSchedules = (schedules) => {
    return schedules.map(scheduleId => {
      const parts = scheduleId.split('-');
      const artist = parts[0];
      const place = parts.slice(1, -2).join('-'); // 最後の2つ以外の部分を再結合
      const start = parts[parts.length - 2];
      const end = parts[parts.length - 1];
      return { artist, place, start, end };
    }).sort((a, b) => a.start.localeCompare(b.start));
  };

  const schedules = getSchedules();

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  const handleNavigate = (path) => {
    navigate(path);
    setMenuOpen(false);
  };

  const scrollToSelectedSchedules = () => {
    const element = document.getElementById('selected-schedules');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div>
      <header className="schedule-header">
        <h1>mistFES {date}</h1>
        <div className="header-buttons">
          <button className="scroll-button" onClick={scrollToSelectedSchedules}>
            選択中のスケジュールへ
          </button>
          <button className="hamburger" onClick={toggleMenu}>
            &#9776;
          </button>
        </div>
      </header>
      {menuOpen && (
        <div className="menu">
          <button className="hamburger" onClick={toggleMenu}>
            &#x2715;
          </button>
          <button className="menu-button" onClick={() => handleNavigate('/')}>
            Home
          </button>
          <button className="menu-button" onClick={() => handleNavigate('/6-8')}>
            6/8
          </button>
          <button className="menu-button" onClick={() => handleNavigate('/6-9')}>
            6/9
          </button>
          <div className="menu-artist-links">
            {schedules.map((artistData, index) => (
              <button
                key={index}
                className="menu-artist-button"
                onClick={() => {
                  document.getElementById(artistData.artist).scrollIntoView({ behavior: 'smooth' });
                  setMenuOpen(false);
                }}
              >
                {artistData.artist}
              </button>
            ))}
          </div>
        </div>
      )}
      <main>
        <div className="concert-list">
          {schedules.map((artistData, index) => (
            <div key={index} className="artist" id={artistData.artist}>
              <div className="artist-name">{artistData.artist}</div>
              <div className="artist-schedules">
                <ul>
                  {artistData.schedules.map((schedule, idx) => {
                    const scheduleId = `${artistData.artist}-${schedule.place}-${schedule.start}-${schedule.end}`;
                    const isSelected = selectedSchedules.includes(scheduleId);
                    return (
                      <li
                        key={idx}
                        className={`schedule-item ${isSelected ? 'selected' : ''}`}
                        onClick={() => handleToggleSchedule(scheduleId)}
                      >
                        {schedule.place} - {schedule.start} to {schedule.end}
                      </li>
                    );
                  })}
                </ul>
              </div>
            </div>
          ))}
        </div>
        <div className="selected-schedules" id="selected-schedules">
          <h2>mistFES {date}</h2>
          <ul>
            {selectedSchedules.length > 0 ? (
              getSortedSchedules(selectedSchedules).map((schedule, index) => (
                <li key={index}>
                  {schedule.artist} - {schedule.place} - {schedule.start} to {schedule.end}
                </li>
              ))
            ) : (
              <li>なし</li>
            )}
          </ul>
        </div>
      </main>
    </div>
  );
};

export default SchedulePage;
