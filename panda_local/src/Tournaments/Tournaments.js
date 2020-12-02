import React, { Component } from 'react';
import { Button } from "react-bootstrap";
import history from './../history';

class Tournaments extends Component {

    handleTournamentInputChange(event) {
        console.log(event)
    }

    render() {
        return (
            <div>
                <h1>Tournaments</h1>
                <br></br>

                Search Tournaments: <input type="text" name="searchTournament" onChange={this.handleTournamentInputChange} />
                <br></br>

                <p>Supermajors: </p>
                <Button variant="btn btn-success" onClick={() => history.push('/EVO')}>EVO</Button>
                <Button variant="btn btn-success" onClick={() => history.push('/Genesis')}>Genesis</Button>
                <Button variant="btn btn-success" onClick={() => history.push('/Frostbite')}>Frostbite</Button>

                <p>Majors: </p>
                <Button variant="btn btn-success" onClick={() => history.push('/Glitch')}>Glitch</Button>
                <Button variant="btn btn-success" onClick={() => history.push('/DreamHack')}>DreamHack</Button>
                <Button variant="btn btn-success" onClick={() => history.push('/Smash_Summit')}>Smash Summit</Button>
            </div>
        )
    }
}

export default Tournaments;