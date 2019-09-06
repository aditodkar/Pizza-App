import React, { Component } from 'react';
import axios from 'axios';
import './home.css';
import { Card } from './card';
import { Navbar } from './navbar';

export default class Home extends Component {

    constructor(props) {
        super(props)
        
        this.state = {
            data: ''
        }
    }

    componentDidMount(){
        axios.get(`https://pythonflaskdeploy.herokuapp.com/`).then(res => {
            this.setState({ 
                data: res.data
            });
        })
    }

    sortBy = (key) => {
        this.setState({ data: [...this.state.data].sort((a, b) => a[key] - b[key]) });
    }

    render() {
        return (
        <div>
            <Navbar/>
            <div class="container-fluid">
                <div class="row">
                    <div className="col-12">
                        <div className="dropdownContainer">
                            <button className="btn btn-primary dropdown-toggle mr-4" type="button" data-toggle="dropdown"
                            aria-haspopup="true" aria-expanded="false">Sort Filter</button>

                            <div className="dropdown-menu">
                                <a className="dropdown-item" href="#" onClick={() => this.sortBy('rating')}>Rating</a>
                                <a className="dropdown-item" href="#" onClick={() => this.sortBy('price')}>Price</a>
                            </div>
                        </div>
                    </div>
                    { this.state.data ? 
                        this.state.data.map(val => {
                            return (
                                <div className="col-sm col-md-4 col-lg-3">
                                    <Card imageURL={val.image} location={val.location} price={val.price} name={val.name} rating={val.rating}/>
                                </div>
                            )
                        })
                        : null
                    }
                </div>
            </div>
        </div>
        )
    }
}
