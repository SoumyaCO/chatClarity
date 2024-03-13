import React from "react"
import Chatclarity_logo from '../Assets/chatclarity_logo.png'
import { BsGithub, BsTwitter } from "react-icons/bs"
import { SiLinkedin } from "react-icons/si"
import { FaFacebookF,} from "react-icons/fa"


const Footer = () => {
  return (
    <div className="footer-wrapper">
      <div className="footer-section-one">
        <div className="footer-logo-container">
          <img src={Chatclarity_logo} alt="" />
        </div>
        <div className="footer-icons">
          <BsTwitter />
          <SiLinkedin />
          <BsGithub/>
          <FaFacebookF />
        </div>
      </div>
      <div className="footer-section-two">
        <div className="footer-section-columns">
          <span>Home</span>
          <span>Help</span>
          <span>About</span>
        </div>
        <div className="footer-section-columns">
          <span>+91 6295311955</span>
          <span>abc@gmail.com</span>
          <span>abc@gmail.com</span>
          <span>contactus@gmail.com</span>
        </div>
        <div className="footer-section-columns">
          <span>Terms & Conditions</span>
          <span>Privacy Policy</span>
        </div>
      </div>
    </div>
  )
}

export default Footer
