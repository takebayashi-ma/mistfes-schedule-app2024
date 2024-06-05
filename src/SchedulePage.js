import React, { useEffect, useState, useRef } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import html2canvas from 'html2canvas';
import './App.css';
import data6_8 from './data6_8.json';
import data6_9 from './data6_9.json';

const SchedulePage = ({ date }) => {
  const [concerts, setConcerts] = useState([]);
  const [selectedSchedules, setSelectedSchedules] = useState(new Set());
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const artistRefs = useRef({});
  const navigate = useNavigate();

  useEffect(() => {
    const data = date === '6/8' ? data6_8 : data6_9;
    const sortedData = [...data].sort((a, b) => a.artist.localeCompare(b.artist));
    setConcerts(sortedData);

    const storedSchedules = JSON.parse(localStorage.getItem(`selectedSchedules${date}`));
    if (storedSchedules) {
      setSelectedSchedules(new Set(storedSchedules));
    }
  }, [date]);

  const handleScheduleToggle = (artist, place, start, end) => {
    const scheduleId = `${artist}-${place}-${start}-${end}`;
    setSelectedSchedules(prevSelected => {
      const newSelected = new Set(prevSelected);
      if (newSelected.has(scheduleId)) {
        newSelected.delete(scheduleId);
      } else {
        newSelected.add(scheduleId);
      }
      localStorage.setItem(`selectedSchedules${date}`, JSON.stringify(Array.from(newSelected)));
      return newSelected;
    });
  };

  const isSelected = (artist, place, start, end) => {
    return selectedSchedules.has(`${artist}-${place}-${start}-${end}`);
  };

  const handleDownloadImage = () => {
    const element = document.getElementById('selected-schedules');
    html2canvas(element).then(canvas => {
      const image = canvas.toDataURL('image/png');
      const newWindow = window.open('', '_blank');
      newWindow.document.write(`
        <html>
          <head>
            <title>Selected Schedules</title>
            <style>
              body {
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #121212;
                flex-direction: column;
              }
              img {
                max-width: 100%;
                max-height: 80vh;
                object-fit: contain;
              }
            </style>
          </head>
          <body>
            <img src="${image}" alt="Selected Schedules" />
          </body>
        </html>
      `);
      newWindow.document.close();
    });
  };

  const scrollToElement = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start', inline: 'nearest' });
      setIsMenuOpen(false);
    }
  };

  const scrollToArtist = (artist) => {
    artistRefs.current[artist].scrollIntoView({ behavior: 'smooth', block: 'start', inline: 'nearest' });
    setIsMenuOpen(false);
  };

  const handleLinkClick = (path) => {
    setIsMenuOpen(false);
    navigate(path);
  };

  const getSortedSchedules = () => {
    const schedulesArray = Array.from(selectedSchedules).map(scheduleId => {
      const [artist, place, start, end] = scheduleId.split('-');
      return { artist, place, start, end };
    });

    schedulesArray.sort((a, b) => a.start.localeCompare(b.start));
    return schedulesArray;
  };

  return (
    <div>
      <header className="schedule-header">
        <h1>mistFES {date}</h1>
        <div className="header-buttons">
          <button className="scroll-button" onClick={() => scrollToElement('selected-schedules')}>
            選択中のスケジュールへ
          </button>
          <button className="hamburger" onClick={() => setIsMenuOpen(!isMenuOpen)}>
            ☰
          </button>
        </div>
      </header>
      {isMenuOpen && (
        <nav className="menu">
          <button className="hamburger" onClick={() => setIsMenuOpen(false)}>
            ☰
          </button>
          <Link to="/" className="menu-link" onClick={() => setIsMenuOpen(false)}>Home</Link>
          <button className="menu-link" onClick={() => handleLinkClick('/6-8')}>6/8</button>
          <button className="menu-link" onClick={() => handleLinkClick('/6-9')}>6/9</button>
          {concerts.map((artistData, index) => (
            <button key={index} className="menu-artist-button" onClick={() => scrollToArtist(artistData.artist)}>
              {artistData.artist}
            </button>
          ))}
        </nav>
      )}
      <nav className="date-links">
        <Link to="/6-8" className="nav-link">6/8</Link>
        <Link to="/6-9" className="nav-link">6/9</Link>
      </nav>
      <main>
        <section className="concert-list">
          {concerts.map((artistData, index) => (
            <div key={index} className="artist-row" id={artistData.artist} ref={el => artistRefs.current[artistData.artist] = el}>
              <div className="artist-name">
                <h2>{artistData.artist}</h2>
              </div>
              <div className="artist-schedules">
                <ul>
                  {artistData.schedules.map((schedule, idx) => (
                    <li
                      key={idx}
                      className={`schedule-item ${isSelected(artistData.artist, schedule.place, schedule.start, schedule.end) ? 'selected' : ''}`}
                      onClick={() => handleScheduleToggle(artistData.artist, schedule.place, schedule.start, schedule.end)}
                    >
                      {schedule.place} - {schedule.start} to {schedule.end}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          ))}
        </section>
      </main>
      <section className="selected-schedules" id="selected-schedules">
        <h2>mistFES {date}</h2>
        <ul>
          {Array.from(selectedSchedules).length > 0 ? (
            getSortedSchedules().map((schedule, index) => (
              <li key={index} onClick={() => scrollToArtist(schedule.artist)}>
                {schedule.artist} - {schedule.place} - {schedule.start} to {schedule.end}
              </li>
            ))
          ) : (
            <li>なし</li>
          )}
        </ul>
      </section>
      <button onClick={handleDownloadImage} className="download-button">画像で表示</button>
      <footer className="footer">
        &copy; bemarble
      </footer>
    </div>
  );
};

export default SchedulePage;
