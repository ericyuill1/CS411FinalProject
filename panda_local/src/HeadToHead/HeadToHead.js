import React, { Component } from "react";
import { useState } from 'react'
import { Button } from "react-bootstrap";
import history from './../history';

export default class HeadToHead extends Component {

    constructor() {
        super();
        this.state = { p1: "", p2: "", showMessage: false};

        this.handleP1InputChange = this.handleP1InputChange.bind(this);
        this.handleP2InputChange = this.handleP2InputChange.bind(this);
        //this.handleVS = this.handleVS.bind(this);
    }
    _showMessage = (bool) => {
        this.setState({
          showMessage: bool
        });
      }

    

    handleP1InputChange(event) {
        this.setState({p1: event.target.value});
        console.log(event)
    }

    handleP2InputChange(event) {
        this.setState({p2: event.target.value});
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
                        <input class = "center" type="text" name="searchPlayer" onChange={this.handleP1InputChange} />
                    </td>
                    VS
                    <td>
                        <input type="text" name="searchPlayer" onChange={this.handleP2InputChange} />
                    </td>
                </tr>
            </table>
        </center>

        <button onClick={this._showMessage.bind(null, true)}>Fight</button>
        <button onClick={this._showMessage.bind(null, false)}>Adjourn</button>
        <br></br>
            { this.state.showMessage && (

            <div>   
                <br></br>

                {this.state.p1} elo:

                <br></br>
                
                {this.state.p2} elo: 
                
                <br></br>
            
            </div>
            
            )}

        </div>
        )
    }
}
