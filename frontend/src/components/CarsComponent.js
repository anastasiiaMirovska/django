import React, {useEffect, useState} from 'react';
import {carService} from "../services/carService";
import CarComponent from "./CarComponent";
import {socketService} from "../services/socketService";

const CarsComponent = () => {
    const [cars, setCars] = useState([]);
    const [trigger, setTrigger] = useState(null);

    useEffect(() => {
        carService.getAll().then(({data})=>setCars(data))
    }, [trigger]);

    useEffect(() => {
        socketInit().then()
    }, []);

    const socketInit = async()=>{
        const {car} = await socketService();
        const client = await car();

        client.onopen = ()=>{
            console.log('CarSocket connected');
            client.send(JSON.stringify({
                action: 'subscribe_to_car_activity',
                request_id: new Date().getTime()
            }))
        }

        client.onmessage = ()=>{
            setTrigger(prev=>!prev)
        }
    }


    return (
        <div>
            {
                cars.map(car=><CarComponent key={car.id} car={car}/>)
            }
        </div>
    );
};

export default CarsComponent;