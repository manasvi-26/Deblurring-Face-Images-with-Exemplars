import React from 'react';
import { BrowserRouter as Router, Route ,Routes} from "react-router-dom";

import Home from './components/Home'
import Carousel from './components/Deblur'

function App() {
  return (
    <Router>
    <Routes>
      <Route path="/" exact element={<Home/>} />
      <Route path="/deblur" exact element={<Carousel/>} />
      
    </Routes>
    </Router>
  );
}

export default App;