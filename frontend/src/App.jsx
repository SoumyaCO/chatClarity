import "./App.css";


import NeverMiss from "./components/NeverMiss"
import Footer from "./components/Footer"
import FileUploder from "./components/FileUploder"
const App = () => {
  return (
    <div className='container'>
     <NeverMiss/>
     {/* <FileUploder/> */}
      <Footer/>
    </div>
  )
}

export default App