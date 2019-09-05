import React from 'react';
import './card.css';

export const Card = ({imageURL, location, price, name, rating}) => (
    <div className="card">
        <img className="card-img-top" src={`${imageURL}`} alt="Card image cap"/>
        <div className="card-body">
        <h4 className="card-title"><a>{name}</a></h4>
        <p className="card-text"><strong>Rating:</strong> {rating}</p>
        <p className="card-text"><strong>Price:</strong> {price}</p>
        <p className="card-text"><strong>Location:</strong> {location}</p>
        </div>
    </div>
)