import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

// HEADER & FOOTER
import BlogLayout from './layouts/BlogLayout/BlogLayout';

// PAGES
import Home from './pages/Home/Home';
import ServicesPage from './pages/ServicesPage/ServicesPage';
import ServicePage from './pages/ServicePage/ServicePage';
import About from './pages/About/About';
import NotFound from './pages/NotFound/NotFound';

// MAIN STYLES
import './index.css';

createRoot(document.getElementById('root')).render(
  <Router>
    <Routes>
      <Route path='/' element={<Navigate to="/home" replace/>} />
      {/* PAGE LAYOUT */}
      <Route path='/' element={<BlogLayout />}>
        <Route path='home' element={<Home />} />
        <Route path='services' element={<ServicesPage />} />
        <Route path='services/:serviceId' element={<ServicePage />} />
        <Route path='about' element={<About />} />
      </Route>
      {/* PAGE NOT FOIND */}
      <Route path='*' element={<NotFound />} />
    </Routes>
  </Router>
);
