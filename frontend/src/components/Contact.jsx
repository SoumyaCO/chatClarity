import React, { useState, useRef } from "react";
import emailjs from "@emailjs/browser";
import Navbar from './Navbar'

const Contact = () => {
  const form = useRef();
  const [showAlert, setShowAlert] = useState(false);

  const sendEmail = (e) => {
    e.preventDefault();

    emailjs.sendForm(
      'service_33il4fj',
      'template_qi0p9yn', 
      form.current,
      'IK1wTU307RAAInBkp' 
    )
    .then(
      (response) => {
        console.log('SUCCESS!',response);
        setShowAlert(true);
      },
      (error) => {
        console.error('FAILED...',error);
      }
    );
  };

  return (
    <div>
      <Navbar/>
      <div className="contact_us">
        <form ref={form} onSubmit={sendEmail}>
          <label>Name</label>
          <input type="text" name="user_name" />
          <label>Email</label>
          <input type="email" name="user_email" />
          <label>Message</label>
          <textarea name="message" />
          <input type="submit" value="Send" />
        </form>
        {showAlert && (
          <div className="alert_message">
            Message sent successfully!
            <button onClick={() => 
              window.location.reload()}> OK</button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Contact;
