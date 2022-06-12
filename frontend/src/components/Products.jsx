import React, { useState, setState, useEffect } from 'react';
import axios from "axios";
import styled from 'styled-components';
import { popularProducts } from '../data';
import Product from './Product';


const Container = styled.div`
    padding: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
`;


const Products = (props) => {
    const [data, setData] = useState([]);

    useEffect(() =>{
        getPopularItems();
    }, []);

    const getPopularItems = async () => {
        await axios.get("http://127.0.0.1:8000/api/pp/"+props.limit).then(res => {
        setData(res.data.pp);
        }).catch(err => console.log(err));
        
    }


  return (
    <Container>
        {data.map(item => (
            <Product item={item} key={item.id}/>
        ))}
    </Container>
      
  )
}

export default Products
