import xarray as xr
import matplotlib.pyplot as plt

def process_file(filepath, level, min_lon, max_lon, min_lat, max_lat):
    ret_list = list()
    
    dataset = xr.open_dataset(filepath)

    if level not in dataset.coords['level'].data:
        raise Exception("No such level exist in NC file")

    lon_list = list()
    for lon in dataset.coords['lon'].data:
        if lon >= min_lon and lon <= max_lon:
            lon_list.append(lon)        

    lat_list = list()
    for lat in dataset.coords['lat'].data:
        if lat >= min_lat and lat <= max_lat:
            lat_list.append(lat)

    is_not_first_foreach = False
    for lon in lon_list:
        print("Work with longitude " + str(lon))
        for lat in lat_list:
            print("Work with latitude " + str(lat))
            dataset_local = dataset.sel(lat=lat, lon=lon, level=level)       
            for idx, air in enumerate(dataset_local.data_vars['air'].data):
                if is_not_first_foreach == True:
                    ret_list[idx][1] = (ret_list[idx][1] + air) / 2

                    # Just to be on the safe side - check time equality
                    if ret_list[idx][0] != dataset_local.coords['time'].data[idx]:
                        raise Exception("Time mismatch for different coords. Abort calculating. Say to developer that he is govnodel")
                else:
                    ret_list.append([dataset_local.coords['time'].data[idx], air])
            
            is_not_first_foreach = True


    return ret_list

def save_to_ascii_file(data_list, out_filepath, header=[]):
    write_list = []

    for data in data_list:
        output_str = ""
        for val in data:
            output_str += str(val) + "\t"
        output_str = output_str[:-1]
        output_str += "\n"
        write_list.append(output_str)

    with open(out_filepath,"w") as f:
        f.writelines(write_list)

def print_graph_data(data_list, out_filepath):
    x = list()
    y = list()

    for data in data_list:
        x.append(data[0])
        y.append(data[1])

    plt.plot(x, y, 'r-')

    # Show the plot
    plt.show()

def main():
    # Open file or select needed
    filepath = "./input/air.2016.nc"

    # Process file
    data_list = process_file(filepath, 1000, 0.0, 5, 80.0, 90.0)

    # Save to ASCII file with tab separator
    save_to_ascii_file(data_list, "./output/out.txt")

    # Print graph
    print_graph_data(data_list, "./output/out.png")

if __name__ == "__main__":
    main()