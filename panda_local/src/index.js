import React from "react";
import ReactDOM from 'react-dom'
import {BrowserRouter as Router } from 'react-router-dom'
import './index.css'
import "bootstrap/dist/css/bootstrap.min.css";
import App from './App'


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


ReactDOM.render(
    <Router>
        <App />
    </Router>
, 
document.getElementById('root'))
// ReactDOM.render(<M_Button/>, document.getElementById('tournaments'))