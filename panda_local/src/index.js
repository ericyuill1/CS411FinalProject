// import React, {useState} from 'react'
// import ReactDOM from 'react-dom'
// import { Navbar, Nav, NavItem, NavDropdown, MenuItem, Form, FormControl, Button } from 'react-bootstrap';

// import Melee from "./components/Melee"
// import Ultimate from "./components/Ultimate"

// const M_Button = (props) => (
//   <button onClick = {props.handleClick}>
//     Melee
//   </button>
// )

// const U_Button = (props) => (
//   <button onClick = {props.handleClick}>
//     Ultimate
//   </button>
// )

// const Nav_bar = () => {
//   return (
//     <Navbar bg="light" expand="lg">
//   <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
//   <Navbar.Toggle aria-controls="basic-navbar-nav" />
//   <Navbar.Collapse id="basic-navbar-nav">
//     <Nav className="mr-auto">
//       <Nav.Link href="#home">Home</Nav.Link>
//       <Nav.Link href="#link">Link</Nav.Link>
//       <NavDropdown title="Dropdown" id="basic-nav-dropdown">
//         <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
//         <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
//         <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
//         <NavDropdown.Divider />
//         <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
//       </NavDropdown>
//     </Nav>
//     <Form inline>
//       <FormControl type="text" placeholder="Search" className="mr-sm-2" />
//       <Button variant="outline-success">Search</Button>
//     </Form>
//   </Navbar.Collapse>
// </Navbar>
//   )
  
// }

// const App = () => {

//   const [ melee, setMelee ] = useState("")
//   const [ ultimate, setUltimate ] = useState("")

//   const M_handleClick = () => {
//     return (
//       <div>
//         melee_data
//       </div>
//     )
//   }
  
//   const U_handleClick = () => {
//     return (
//       <div>
//         ultimate_data
//       </div>
//     )
//   }

//   const Bar = () => {
//     return (
//       <div>
//         PandasLocal
//       </div>
//     )
//   }


//   return (
//     <div>
//       <Nav_bar/>
//       <Bar/>
//       <M_Button handleClick = {M_handleClick}/>
//       <U_Button handleClick = {U_handleClick}/>
//     </div>
//   )

//   }

// //done

// ReactDOM.render(<App />, document.getElementById('root'))

import React from "react";
import ReactDOM from 'react-dom'

import "bootstrap/dist/css/bootstrap.min.css";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import FormControl from "react-bootstrap/FormControl";
import NavDropdown from "react-bootstrap/NavDropdown";

export default function App() {
  return (
    <div>
      <Navbar bg="light" expand="lg">
        <Navbar.Brand href="#home">Panda Local</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse>
          <Nav className="mr-auto">
            <Nav.Link href="/test.js">Tournaments</Nav.Link>
            <Nav.Link href="/headtohead.html">Head to Head</Nav.Link>
            <Nav.Link href="#home">crud</Nav.Link>
            <NavDropdown title="Games">
              <NavDropdown.Item href="#action/1">Melee</NavDropdown.Item>
              <NavDropdown.Item href="#action/2">Ultimate</NavDropdown.Item>
            </NavDropdown>
          </Nav>
          <Form inline>
            <FormControl type="text" placeholder="search" className="mr-sm-2" />
            <Button variant="outline-primary">search</Button>
          </Form>
        </Navbar.Collapse>
      </Navbar>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'))