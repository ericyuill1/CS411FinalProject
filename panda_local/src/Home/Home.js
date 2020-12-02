import React, { Component } from "react";
import { Button } from 'react-bootstrap';
import history from './../history';
import "./Home.css";
const axios = require('axios');
export default class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            result: "",
        }
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSearch = this.handleSearch.bind(this);
    }
    handleSearch(event) {
        axios.post('/insert', {
            tag: "MkLeo",
        })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            })
            .then(function () {
                // always executed
                console.log("I always run");
            });
    }

    handleInputChange(event) {
        console.log(event);
    }

    render() {
    return (
        <div className="Home">
        <div className="lander">
            <h1>Home page</h1>
            <p>A simple app showing react button click navigation</p>
            <form>
            <input type="text" name="searchPlayer" onChange={this.handleInputChange} />
            </form>
        </div>
        </div>
    );
}
}