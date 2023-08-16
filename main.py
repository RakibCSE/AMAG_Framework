from framework.vehicle_data import VehicleData


if __name__ == '__main__':
    data_path = './data.npy'
    
    # VehicleData instance
    obj = VehicleData(data_path)
    
    id_data = obj.get_data_by_id(4)
    
    print(len(id_data))

    