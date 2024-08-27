import React, {useEffect, useState} from 'react';
import {carService} from "../services/carService";
import CarComponent from "./CarComponent";

const CarsComponent = () => {
    const [cars, setCars] = useState([]);
    useEffect(() => {
        carService.getAll().then(({data})=>setCars(data))
    }, []);
    return (
        <div>
            {
                cars.map(car=><CarComponent key={car.id} car={car}/>)
            }
        </div>
    );
};

export default CarsComponent;