import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

// HEADER
import AppLayout from './layouts/AppLayout/AppLayout';

// PAGES
import Home from './pages/Home/Home';
import Contacnts from './pages/Contacts/Contacts';
import AddContact from './pages/AddContact/AddContact';
import NotFound from './pages/NotFound/NotFound';

// MAIN STYLE
import './index.css'

// Заменить на подсчет записей 
const counter = 0;

createRoot(document.getElementById('root')).render(
  <Router>
    <Routes>
      <Route path='/' element={<Navigate to="/home" replace/>} />
      {/* PAGE LAYOUT */}
      <Route path='/' element={<AppLayout />}>
        <Route path='home' element={<Home counter={counter} />} />
        <Route path='contacts' element={<Contacnts />} />
        <Route path='add-contact' element={<AddContact />} />
      </Route>
      {/* PAGE NOT FOIND */}
      <Route path='*' element={<NotFound />} />
    </Routes>
  </Router>
)
