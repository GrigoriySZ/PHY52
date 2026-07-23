import { useState, useEffect, useReducer } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { contactReducer } from "./reducer/contactsReducer";

// PAGES
import Home from './pages/Home/Home';
import Contacnts from './pages/Contacts';
import AddContact from './pages/AddContact';
import NotFound from './pages/NotFound';
import AppLayout from './layouts/AppLayout/AppLayout';

const initialState = {
  contacts: [
    {id: 1, name: "Иванов Иван", phone: "+7(999)777-55-33"},
    {id: 2, name: "Петрова Анна", phone: "+7(913)766-51-66"},
    {id: 3, name: "Балагуров Афанасий", phone: "+7(901)765-52-12"},
    {id: 4, name: "Таврова Ульяна", phone: "+7(921)684-10-98"},
    {id: 5, name: "Ильниа Ульяна", phone: "+7(910)456-16-14"}
  ],
};

export default function App() {
  const [state, dispatch] = useReducer(contactReducer, initialState);
  const [sorageLimit, setStorageLimit] = useState(20);

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<Navigate to="/home" replace/>} />
          {/* PAGE LAYOUT */}
          <Route path='/' element={<AppLayout />}>
            <Route path='home' element={
              <Home contacts={state.contacts} contactsLimit={sorageLimit}/>
            } />
            <Route path='contacts' element={
              <Contacnts contacts={state.contacts} dispatch={dispatch}/>
            } />
            <Route path='add-contact' element={<AddContact />} />
          </Route>
          {/* PAGE NOT FOUND */}
          <Route path='*' element={<NotFound />} />
        </Routes>
      </Router>
    </>
  )
};