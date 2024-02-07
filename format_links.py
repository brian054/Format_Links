def format_links_as_string(links, delimiter): 
    formatted_links = delimiter.join(f"{link.strip()}" for link in links)
    return formatted_links


def main():
    try:
        with open("links.txt", "r") as file:
            links = file.readlines()
    except FileNotFoundError:
        print("Error: The 'links.txt' file was not found.")
        return

    formatted_string = format_links_as_string(links, ",")
    print("Formatted Links:")
    print(formatted_string)


if __name__ == "__main__":
    main()
