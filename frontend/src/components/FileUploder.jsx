import React, { useState } from "react";
import { MdCloudUpload, MdDelete } from "react-icons/md";
import { FaFile } from "react-icons/fa";
import Output from "./Output";
import Plot from "react-plotly.js";

export let api_fetch_data = {};

export const FileUploader = () => {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState("No selected file");
  const [selectedDate, setSelectedDate] = useState(null);
  const [showOutput, setShowOutput] = useState(false);
  const [apiResponse, setApiResponse] = useState(null);
  const [apiData, setApiData] = useState({ users: [], counts: [] });

  const handleQuery = async () => {
    // Get the file, date, and time from the form
    const fileInput = document.getElementById("fileInput");
    const date = document.getElementById("dateInput").value;

    // Create a formdata
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);
    formData.append("date", date);

    const response = await fetch("http://127.0.0.1:5000/test", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => (api_fetch_data = data))
      .catch((error) => console.error("Error: ", error));

    console.log(api_fetch_data)
    // const data = await response.json();
    // setApiResponse(data); // Store the API response

  };

  const handleSubmit = (event) => {
    event.preventDefault();
    handleQuery();
    setShowOutput(true);
  };
  if (showOutput) {
    return <Output data={apiResponse} />;
  }

  return (
    <main>
      <div className="FileUploader">
        <form onSubmit={handleSubmit}>
          <input
            type="file"
            id="fileInput"
            accept=".txt, application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            className="input-field"
            hidden
            onChange={({ target: { files } }) => {
              files[0] && setFileName(files[0].name);
              if (files) {
                setFile(URL.createObjectURL(files[0]));
              }
            }}
          />
          <div
            className="upload_img"
            onClick={() => document.querySelector(".input-field").click()}
          >
            {file ? (
              <>
                <FaFile color="#1475cf" size={60} />
                <p>{fileName}</p>
              </>
            ) : (
              <>
                <MdCloudUpload color="#1475cf" size={60} />
                <p>Browse files to upload</p>
              </>
            )}
          </div>

          <div className="date_picker">
            <label htmlFor="dateInput">Date:</label>
            <input
              className="secondary-button"
              type="date"
              id="dateInput"
              onChange={(e) => setSelectedDate(e.target.value)}
            />
          </div>
          <div className="upload_button">
            <button type="submit" className="secondary-button">
              Upload
            </button>
          </div>
        </form>
      </div>
    </main>
  );
}

export default FileUploader;

// {
/* </div>
        <form action="" method="post" enctype="multipart/form-data">
          <input type='file' 
                 accept='.txt, application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document' 
                 className='input-field' 
                 hidden
                 onChange={({target: {files}}) => {
                   files[0] && setFileName(files[0].name)
                   if(files){
                     setFile(URL.createObjectURL(files[0]));
                   }
                 }}
          />
          <div className='upload_img' onClick={() => document.querySelector(".input-field").click()}>
          {file ?
            <>
              <FaFile color='#1475cf' size={60} />
              <p>{fileName}</p>
            </>
            :
            <>
              <MdCloudUpload color='#1475cf' size={60} />
              <p>Browse files to upload</p>
            </>
          }
           
          </div>
          
          <div className='date_picker'>
            <input  className='secondary-button'type='date' onChange={(e) => setSelectedDate(e.target.value)} />
          </div>
          <div className='upload_button'>
            <button type="submit" className='secondary-button'>Upload</button>
          </div>
        </form> */
// }
// {
/* <section className='uploaded'>
          <FaFile color='#1475cf'/>
          <span className='uploaded-file'>
            {fileName} -
            <MdDelete 
              onClick={() =>{
                setFileName("No selected File");
                setFile(null);
              }}
            />
          </span>
        </section>
        
      </div> */
// }
