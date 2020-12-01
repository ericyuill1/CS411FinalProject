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
    console.log(showing);
  return (
    <div>
      <Navbar bg="light" expand="lg">
        <Navbar.Brand href="#home">Panda Local</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse>
          <Nav className="mr-auto">
            <Nav.Link href="/tournaments.html">Tournaments</Nav.Link>
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
      <br></br>
      <p>
          hi
      </p>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'))