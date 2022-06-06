import Home from './pages/Home';
import ProductList from './pages/ProductList';
import Product from './pages/Product';
import Cart from './pages/Cart';

import {BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Home/>
    </div>

  );
}

export default App;
