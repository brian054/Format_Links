def extract_links(input_string):
    links = input_string.split(" | ")
    return links


# for git


def write_to_file(links, output_file):
    with open(output_file, "w") as file:
        for link in links:
            file.write(link + "\n")


if __name__ == "__main__":
    input_file = "raw.txt"
    output_file = "extracted.txt"  # Set the output file name

    try:
        with open(input_file, "r") as file:
            input_string = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    else:
        links = extract_links(input_string)
        write_to_file(links, output_file)

        print(f"Links extracted and written to {output_file}.")
