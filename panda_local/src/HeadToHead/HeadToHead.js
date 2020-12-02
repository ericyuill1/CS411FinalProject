import React, { Component } from "react";
import { Button } from "react-bootstrap";
import history from './../history';

export default class HeadToHead extends Component {
    render () {
        return (
            <div>
                <h1>HeadToHead Page</h1>
                <p>Lorem Ipsum</p>
                <form>
            <Button variant="btn btn-success" onClick={() => history.push('/Tournaments')}>Click button to view products</Button>
          </form>
            </div>
        )
    }
}