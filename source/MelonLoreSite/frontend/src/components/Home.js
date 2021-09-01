import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect
} from 'react-router-dom';

export default class Home extends Component {
    constructor(props){
        super(props)
    }

    render(){
        return (
        <Router>
            <Switch>
                <Route exact path="/">
                    <h1>Welcome Home</h1>
                </Route>
            </Switch>
        </Router>);
    }
}