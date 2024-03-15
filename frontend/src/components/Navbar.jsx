import React, { useState } from "react"
import { HiOutlineBars3 } from "react-icons/hi2"
import Box from "@mui/material/Box"
import Drawer from "@mui/material/Drawer"
import List from "@mui/material/List"
import Divider from "@mui/material/Divider"
import ListItem from "@mui/material/ListItem"
import ListItemButton from "@mui/material/ListItemButton"
import ListItemIcon from "@mui/material/ListItemIcon"
import ListItemText from "@mui/material/ListItemText"
import HomeIcon from "@mui/icons-material/Home"
import InfoIcon from "@mui/icons-material/Info"
import PhoneRoundedIcon from "@mui/icons-material/PhoneRounded"
import Github_logo from '../Assets/Github_logo.png'
import Chatclarity_logo from '../Assets/chatclarity_logo.png'
import {Link} from 'react-router-dom'


const Navbar = () => {
  const [openMenu, setOpenMenu] = useState(false)
  const menuOptions = [
    {
      text: "Home",
      icon: <HomeIcon />,
    },
    {
      text: "About",
      icon: <InfoIcon />,
    },

    {
      text: "Contact us",
      icon: <PhoneRoundedIcon />,
    },
  ]
  return (
    <nav>
      <div className="nav-logo-container">
        <img src={Chatclarity_logo} alt="" className="Logo" />
      </div>
      <div className="navbar-links-container">
        <Link to="/">Home</Link>
        <a href="">About</a>
        <Link to="/contact">Contact us</Link>
        <a href="https://github.com/SoumyaCO/chatClarity">
          <img src={Github_logo} alt="" className="navbar-github-icon" />
        </a>
      </div>
      <div className="navbar-menu-container">
        <HiOutlineBars3 onClick={() => setOpenMenu(true)} />
      </div>
      <Drawer open={openMenu} onClose={() => setOpenMenu(false)} anchor="right">
        <Box
          sx={{ width: 250 }}
          role="presentation"
          onClick={() => setOpenMenu(false)}
          onKeyDown={() => setOpenMenu(false)}
        >
          <List>
            {menuOptions.map((item) => (
              <ListItem key={item.text} disablePadding>
                <ListItemButton>
                  <ListItemIcon>{item.icon}</ListItemIcon>
                  <ListItemText primary={item.text} />
                </ListItemButton>
              </ListItem>
            ))}
          </List>
          <Divider />
        </Box>
      </Drawer>
    </nav>
  );
}

export default Navbar