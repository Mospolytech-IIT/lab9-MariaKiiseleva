import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import TextField from '@mui/material/TextField'
import { Button, Stack, Typography } from '@mui/material'
import axios from 'axios'
import CreatePage from './pages/create_page'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import GetPage from './pages/get_page'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/create" element={<CreatePage/>}></Route>
        <Route path="/get" element={<GetPage/>}></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
