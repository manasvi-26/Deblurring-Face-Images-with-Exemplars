import React, { useState} from "react";
import "./Deblur.css";
import { all_images } from "../Helpers/CarouselData";
import ArrowBackIosIcon from "@material-ui/icons/ArrowBackIos";
import ArrowForwardIosIcon from "@material-ui/icons/ArrowForwardIos";

import {useLocation} from 'react-router-dom'

function Carousel(props) {
  const [currImg, setCurrImg] = useState(0);

  const { state } = useLocation();
  const image_index = state.image
  console.log(image_index)

  const images = all_images[image_index]

  return (
      <>
    <div className="carousel" style={{float:"left"}}>
      <div
        className="carouselInner"
        style={{ backgroundImage: `url(${images[currImg].img})` }}
        >
        <div
          className="left"
          onClick={() => {
            currImg > 0 && setCurrImg(currImg - 1);
          }}
        > 
          <ArrowBackIosIcon style={{ fontSize: 30 }} />
        </div>
        <div className="center">
          <p>{images[currImg].subtitle}</p>
        </div>
        <div
          className="right"
          onClick={() => {
            currImg < images.length - 1 && setCurrImg(currImg + 1);
          }}
        >
          <ArrowForwardIosIcon style={{ fontSize: 30 }} />
        </div>
      </div>
    </div>
    <div  style={{backgroundColor:"red" , float:"left"}}>
           Test para
    </div>
    </>
  )
}

export default Carousel;