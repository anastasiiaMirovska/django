import React from 'react';

const CarComponent = ({car}) => {
    const {brand, price, year, body_type} = car;
    return (
        <div>
            <div>brand: {brand}</div>
            <div>price: {price}</div>
            <div>year: {year}</div>
            <div>body_type: {body_type}</div>
        </div>
    );
};

export default CarComponent;