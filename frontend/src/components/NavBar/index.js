import React from "react";
import {
    Nav,
    NavLink,
    Bars,
    NavMenu,
    NavBtn,
    NavBtnLink,
} from "./NavbarElements";

const NavBar = () => {
    return (
        <>
           <Nav>
                <Bars />
                <NavMenu>
                    <NavLink to="/" >
                        Visualizations
                    </NavLink>
                    <NavLink to="/analysis" activeStyle>
                        Analysis
                    </NavLink>
                    {/* Second Nav */}
                    {/* <NavBtnLink to='/sign-in'>Sign In</NavBtnLink> */}
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;