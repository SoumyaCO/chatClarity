import React, { useState } from 'react';
import { MdCloudUpload, MdDelete } from 'react-icons/md';
import { AiFillFileImage } from 'react-icons/ai';

function FileUploader() {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState("No selected file");

  return (
    <main>
      <div className='FileUploader'>
        <form 
          onClick={() => document.querySelector(".input-field").click()}
        >
          <input type='file' 
                 accept='.doc,.pdf,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document' 
                 className='input-field' 
                 hidden
                 onChange={({target: {files}}) => {
                   files[0] && setFileName(files[0].name)
                   if(files){
                     setFile(URL.createObjectURL(files[0]));
                   }
                 }}
          />
          <div className='upload_img'>
          {file ?
            <>
              <AiFillFileImage color='#1475cf' size={60} />
              <p>{fileName}</p>
            </>
            :
            <>
              <MdCloudUpload color='#1475cf' size={60} />
              <p>Browse files to upload</p>
            </>
          }
           
          </div>
         
        </form>
        <section className='uploaded'>
          <AiFillFileImage color='#1475cf'/>
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
        <div className='upload_button'>
            <button className='secondary-button'>Upload</button>
          </div>
      </div>
    </main>
  )
}

export default FileUploader;
