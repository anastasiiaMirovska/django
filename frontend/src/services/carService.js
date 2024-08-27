import {apiService} from "./apiService";

const carService = {
    getAll(){
        return apiService.get(urls.cars);
    },
    create(data){
        return apiService.post(urls.cars, data)
    }
}


export{
    carService
}