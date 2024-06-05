import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import html2canvas from 'html2canvas';
import './App.css';
import data6_8 from './data6_8.json';
import data6_9 from './data6_9.json';

const Home = () => {
  const [selectedSchedules6_8, setSelectedSchedules6_8] = useState([]);
  const [selectedSchedules6_9, setSelectedSchedules6_9] = useState([]);

  useEffect(() => {
    const storedSchedules6_8 = JSON.parse(localStorage.getItem('selectedSchedules6/8')) || [];
    const storedSchedules6_9 = JSON.parse(localStorage.getItem('selectedSchedules6/9')) || [];
    setSelectedSchedules6_8(storedSchedules6_8);
    setSelectedSchedules6_9(storedSchedules6_9);
  }, []);

  const getSortedSchedules = (schedules) => {
    return schedules.map(scheduleId => {
      const [artist, place, start, end] = scheduleId.split('-');
      return { artist, place, start, end };
    }).sort((a, b) => a.start.localeCompare(b.start));
  };

  const handleDownloadImage = () => {
    const element = document.getElementById('combined-schedules');
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

  return (
    <div>
      <header className="schedule-header">
        <h1>mistFES2024マイタイムテーブル</h1>
      </header>
      <div className="info-text">
        参加予定のスケジュールを追加しましょう
      </div>
      <main>
        <section className="selected-schedules" id="combined-schedules">
          <h2><Link to="/6-8" className="nav-link">mistFES 6/8</Link></h2>
          <ul>
            {selectedSchedules6_8.length > 0 ? (
              getSortedSchedules(selectedSchedules6_8).map((schedule, index) => (
                <li key={index}>
                  {schedule.artist} - {schedule.place} - {schedule.start} to {schedule.end}
                </li>
              ))
            ) : (
              <li>なし</li>
            )}
          </ul>
          <h2><Link to="/6-9" className="nav-link">mistFES 6/9</Link></h2>
          <ul>
            {selectedSchedules6_9.length > 0 ? (
              getSortedSchedules(selectedSchedules6_9).map((schedule, index) => (
                <li key={index}>
                  {schedule.artist} - {schedule.place} - {schedule.start} to {schedule.end}
                </li>
              ))
            ) : (
              <li>なし</li>
            )}
          </ul>
        </section>
      </main>
      <button onClick={handleDownloadImage} className="download-button">画像で表示</button>
      <footer className="footer">
        &copy; bemarble
      </footer>
    </div>
  );
};

export default Home;
