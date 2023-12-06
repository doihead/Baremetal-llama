

def bin_to_c_array(bin_file_path, header_file_path, array_name, n_items_per_line=256):
    """
    Converts the contents of a binary file into a C array in a header file.

    :param bin_file_path: Path to the binary file.
    :param header_file_path: Path to the output header file.
    :param array_name: Name of the C array.
    """
    try:
        # Read the binary file
        with open(bin_file_path, 'rb') as bin_file:
            data = bin_file.read()

        # Convert the data to a C array format
        c_array_lines = []
        for i in range(0, len(data), n_items_per_line):
            # print(i, len(data))
            line = ', '.join(f'0x{byte:02X}' for byte in data[i:i + n_items_per_line])
            c_array_lines.append(line)
            
            if i % (n_items_per_line * 100) == 0:
                print(f"Progress: {i/len(data)*100:.2f}%")
            
            # if i > 1024:
            #     break

        formatted_c_array = ',\n'.join(c_array_lines)

        # Write to the header file
        with open(header_file_path, 'w') as header_file:
            header_file.write("#pragma once\n\n")
            header_file.write(f'unsigned char {array_name}[] = {{\n{formatted_c_array}\n}};\n')

        print(f"C array written to {header_file_path}")

    except IOError as e:
        print(f"An error occurred: {e}")

bin_to_c_array(
    "./stories260K.bin",
    # "./stories15M.bin",
    "./weights.h",
    "WEIGHTS"
)
bin_to_c_array(
    "./tok512.bin",
    # "./stories15M.bin",
    "./tokenizer.h",
    "TOKENIZER"
)