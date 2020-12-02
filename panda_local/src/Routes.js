import React, { Component } from "react";
import { Router, Switch, Route } from "react-router-dom";
import history from './history';
import Home from "./Home/Home";
import HeadToHead from "./HeadToHead/HeadToHead"
import Tournaments from "./Tournaments/Tournaments"
export default class Routes extends Component {
    render() {
        return (
            <Router history={history}>
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/Tournaments" exact component={Tournaments} />
                    <Route path="/HeadToHead" exact component={HeadToHead} />
                    {/* <Route path="/Contact" component={Contact} /> */}
                    {/* <Route path="/Products" component={Products} /> */}
                </Switch>
            </Router>
        )
    }
}