import React, { useState, setState, useEffect } from 'react';
import styled from 'styled-components';
import {categories} from "../data"
import CategoryItem from './CategoryItem';
import axios from "axios";


const Container = styled.div`
    display: flex;
    padding: 20px;
    justify-content: space-between;
`;

const Categories = () => {

  const [data, setData] = useState([]);

  useEffect(() =>{
    get3Categories();
  }, []);

  const get3Categories = async () => {
    await axios.get("http://127.0.0.1:8000/api/categories/3").then(res => {
    setData(res.data.categories);
    }).catch(err => console.log(err));
    
}


  return (
    <Container>
        {data.map(item => (
            <CategoryItem item={item}/>
        ))}
    </Container>

  )
}

export default Categories
