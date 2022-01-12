import * as React from 'react';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

import image1 from '../Images/1/Blurred.jpg'
import image2 from '../Images/2/Blurred.jpg'
import image3 from '../Images/3/Blurred.jpg'
import image4 from '../Images/4/Blurred.jpg'


import { useNavigate } from "react-router-dom";


const Item = styled(Paper)(({ theme }) => ({
  ...theme.typography.body2,
  padding: theme.spacing(3),
  textAlign: 'center',
  // maxHeight:800,
  // maxWidth:8,
  display:"flex",
  color: theme.palette.text.secondary,
}));

export default function Home() {

    const navigate = useNavigate();
    const render_deblur = (val) =>{
        console.log("HELO")
        navigate('/deblur', {
            state: {
                image :  val 
            }
        })
    }

  return (
    <div>
    <h2>Deblurring Face Images Using Exemplars</h2>
    <h3>Which image do you want to deblur?</h3>
    <Box sx={{ flexGrow: 1 , paddingLeft:"8%" }}>
      <Grid container spacing={2} alignItems="center" justifyContent="center">
        <Grid item xs ={8} alignItems="center" justifyContent="center">
          <Item onClick={() => render_deblur(1)}>
            <img src={image1}/>
          </Item>
        </Grid>
        <Grid item xs ={8} alignItems="center" justifyContent="center">
          <Item onClick={() => render_deblur(2)}>
              
              <img src={image2}/>
          </Item>
        </Grid>
        <Grid item xs ={8} alignItems="center" justifyContent="center">
          <Item onClick={() => render_deblur(3)}>
              <img src={image3}/>
          </Item>
        
        </Grid>
        <Grid item xs ={8} alignItems="center" justifyContent="center">
          <Item onClick={() => render_deblur(8)}>
              <img src={image4}/>
          </Item>
        </Grid>
      </Grid>
    </Box>
    </div>
  );
}
