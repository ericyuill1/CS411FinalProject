import React, { Component, useState } from "react";
import { Button } from "react-bootstrap";
import history from './../history';

export default class HeadToHead extends React.Component {

    handleP1InputChange(event) {
        console.log(event)
    }

    handleP2InputChange(event) {
        console.log(event)
    }

    constructor() {
        super(); 
        this.state = { showMessage: false }
      }
    
      _showMessage = (bool) => {
        this.setState({
          showMessage: bool
        });
      }

    render () {
        return (
            <div>
                <h1>HeadToHead</h1>
            
            <br></br>

            <table class = "center">
                <tr>
                    <td>
                        <input type="text" name="searchPlayer" onChange={this.handleP1InputChange} />
                    </td>
                    VS
                    <td>
                        <input type="text" name="searchPlayer" onChange={this.handleP2InputChange} />
                    </td>
                </tr>
            </table>
            
            <button onClick={this._showMessage.bind(null, true)}>show results</button>
            <button onClick={this._showMessage.bind(null, false)}>hide</button>
            { this.state.showMessage && (

            <div>

                player1 elo:

                <br></br>
                
                player2 elo:
                
                <br></br>
            
            </div>
            
            )}

            </div>
        )
    }
}