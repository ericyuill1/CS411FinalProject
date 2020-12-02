import React, { Component } from "react";
import { useState, setState } from 'react'
import { Button } from "react-bootstrap";
import history from './../history';
import axios from 'axios';
import HeadToHeadList from "./../components/HeadToHeadList";
import WithListLoading from "./../components/WithListLoading";
export default class HeadToHead extends Component {

    constructor() {
        super();
        this.state = { 
            p1: "", 
            p2: "", 
            showMessage: false,
            loading: true,
            repos: null,
        };
        this.ListLoading = WithListLoading(HeadToHeadList);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.requestHeadtoHead = this.requestHeadtoHead.bind(this);
        // this.handleP2InputChange = this.handleP2InputChange.bind(this);
        //this.handleVS = this.handleVS.bind(this);
    }
    _showMessage = (bool) => {
        this.setState({
          showMessage: bool
        });
      }
    // ListLoading = withListLoading(HeadToHeadList);
    requestHeadtoHead(event) {
        let headers = new Headers();

        headers.append('Content-Type', 'application/json');
        headers.append('Accept', 'application/json');
        headers.append('Origin','http://localhost:5000');
        var self = this;
        console.log(this.state);
        // console.log(self.state);
        axios({
            url: "/headtohead",
            baseURL: 'http://127.0.0.1:5000',
            method: 'POST',
            headers: headers,
            data: {
                player1: this.state.p1,
                player2: this.state.p2
            },
        })
            .then(function (response) {
                console.log(response.data);
                self.setState({ loading : false, repos: response.data});
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
        const {value, name} = event.target;
        this.setState({
            [name] : value
        });
        console.log(event)
    }
  
    render () {
        return (
        
        <div>
                <h1>HeadToHead</h1>
            
            <br></br>
        <center>
            <table style={{ textAlign: 'center', fontSize: '20px' }}>
                <tr>
                    <td>
                        <input class = "center" type="text" name="p1" value={this.state.p1} onChange={this.handleInputChange} />
                    </td>
                    VS
                    <td>
                        <input type="text" name="p2" value={this.state.p2} onChange={this.handleInputChange} />
                    </td>
                </tr>
            </table>
        </center>

        <button onClick={this._showMessage.bind(null, true)}>Fight</button>
        <button onClick={this._showMessage.bind(null, false)}>Adjourn</button>
        <button onClick={this.requestHeadtoHead}>Show</button>
        <br></br>
            { (

            <div>   
                <br></br>

                {this.state.p1} elo:

                <br></br>
                
                {this.state.p2} elo: 
                
                <br></br>
                <div>
                <this.ListLoading isLoading={this.state.loading} repos={this.state.repos}/>
                </div>
            </div>
            
            )}

        </div>
        )
    }
}
