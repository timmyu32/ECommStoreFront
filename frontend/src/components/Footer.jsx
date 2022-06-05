import React from 'react';
import styled from 'styled-components';
import { AiFillFacebook,  } from "react-icons/ai";
import { ImInstagram } from "react-icons/im";
import { BsTwitter } from "react-icons/bs";
import { IoLocationSharp } from "react-icons/io5";
import { MdEmail } from "react-icons/md";

const Container = styled.div`
    display: flex;
`;

const Logo = styled.h1``;

const Desc = styled.p`
    margin: 20px 0px;

`;

const SocialContainer = styled.div`
    display: flex;
`;

const SocialIcon = styled.div`
    width: 40px;
    height: 40px; 
    border-radius: 50%;   
    color: white;
    background-color: #${props => props.color};
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 20px;

`;


const Left = styled.div`
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 20px;
`;

const Right = styled.div`    
    flex: 1;
    padding: 20px;
`;

const Center = styled.div`    
    flex: 1;
    padding: 20px;

`;

const Title = styled.h3`
    margin-bottom: 30px;
`;

const List = styled.ul`
    margin: 0;
    padding: 0;
    list-style: none;
    display: flex;
    flex-wrap: wrap;

`;

const ListItem = styled.li`
    width: 50%;
    margin-bottom: 10px;

`;

const ContactItem = styled.div`
    margin-bottom: 20px;
    diplay: flex;
    align-items: center;
`;


const Footer = () => {
  return (
    <Container>
        <Left>
            <Logo>ModernMensWear.</Logo>
            <Desc>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus 
                exercitationem reprehenderit dolorem magnam sint officiis nobis officia dolores qui 
                iure nemo vitae atque labore nam totam, quidem maiores, molestiae aspernatur.
            </Desc>
            <SocialContainer>
                <SocialIcon color='3B5999'>
                    <AiFillFacebook/>
                </SocialIcon>
                <SocialIcon color='E4405F'>
                    <ImInstagram/>
                </SocialIcon>
                <SocialIcon color='55ACEE'>
                    <BsTwitter/>
                </SocialIcon>
            </SocialContainer>
        </Left>
        <Center>
            <Title>Useful Links</Title>
            <List>
                <ListItem>Home</ListItem>
                <ListItem>Cart</ListItem>
                <ListItem>Terms </ListItem>
            </List>
        </Center>
        <Right>
            <Title>Contact</Title>
            <ContactItem>
                <IoLocationSharp style={{marginRight:"10px"}}/>
                300 Babcock Street, Boston MA, 02215
            </ContactItem>
            <ContactItem>
                <MdEmail style={{marginRight:"10px"}}/>
                contact@modernmens.com
            </ContactItem>

        </Right>

    </Container>
  )
}

export default Footer
