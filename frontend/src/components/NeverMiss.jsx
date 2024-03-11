import React, { useState } from 'react'
import Navbar from './Navbar'
import FileUploder from './FileUploder'
import BannerBackground from "../Assets/home-banner-background.png"
import home_banner_image from '../Assets/home-banner-image.png'
import { FiArrowRight } from "react-icons/fi"

function NeverMiss() {
  const [showUploader, setShowUploader] = useState(false);

  return (
    <div className='home-container'>
       <Navbar/>
       <div className="home-banner-container">
        <div className="home-bannerImage-container">
          <img src={BannerBackground} alt="" />
        </div>
    <div className='home-text-section'>
     
        {!showUploader && (
          <>
            <h1 className="primary-heading">
              Never miss an important update
            </h1>
            <p className="secondary-text">
              Unlock the hidden potential of your WhatsApp conversations with ChatClarity
            </p>
            <button className="secondary-button" onClick={() => setShowUploader(true)}>
              Get Started <FiArrowRight />{" "}
            </button>
          </>
        )}
        {showUploader && (
          <div className='Upload_file fade-in'>
            <FileUploder/> 
          </div>
        )}
       </div>
      <div className='home-image-section'>
        <img src={home_banner_image} alt=""/>
      </div>
    </div>
    </div>
    
  )
}

export default NeverMiss
