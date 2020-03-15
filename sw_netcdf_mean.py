import xarray as xr

def process_file(filepath, level, s_lon, e_lon, s_lat, e_lat):
    ret_list = list()
    
    dataset = xr.open_dataset(filepath)

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
    # TODO implement
    pass

def main():
    # Open file or select needed
    filepath = "./input/sample"

    # Process file
    data_list = process_file(filepath, 1000, 0.0, 357.5, 60.0, 90.0)

    # Save to ASCII file with tab separator
    save_to_ascii_file(data_list, "./output/out.txt")

    # Print graph
    print_graph_data(data_list, "./output/out.png")

if __name__ == "__main__":
    main()