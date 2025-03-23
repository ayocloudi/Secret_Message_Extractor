import requests
from bs4 import BeautifulSoup

# URL of the Google Doc
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
def fetch_google_doc_html(url):
    """ Fetches the HTML content of the published Google Doc. """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to retrieve document.")

def parse_table(html):
    """ Extracts table data from the HTML document and returns grid data. """
    soup = BeautifulSoup(html, "html.parser")

    # Find the table in the document
    table = soup.find("table")
    if not table:
        raise Exception("No table found in document!")

    grid_data = []
    max_x, max_y = 0, 0 

    # Extract rows and columns
    rows = table.find_all("tr")
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all("td")
        if len(cells) < 3:
            continue  # Skip if the row isn't complete

        try:
            x = int(cells[0].text.strip())
            character = cells[1].text.strip()
            y = int(cells[2].text.strip())

            grid_data.append((character, x, y))
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        except ValueError:
            continue  # Skip rows with invalid data

    # Debugging: Print extracted characters
    extracted_message = ''.join(char for char, _, _ in grid_data)
    print("\nExtracted Letters:", extracted_message)

    return grid_data, max_x, max_y

def create_grid(grid_data, max_x, max_y):
    """ Creates a 2D grid filled with characters based on coordinates. """
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for char, x, y in grid_data:
        grid[y][x] = char  # y = row, x = column

    return grid

def print_grid(grid):
    """ Prints the reconstructed grid. """
    for row in grid:
        print(''.join(row))

def extract_secret_message(grid_data):
    """ Extracts the secret message by reading characters in order. """
    sorted_data = sorted(grid_data, key=lambda item: (item[2], item[1]))  # Sort by (y, x)
    return ''.join(char for char, _, _ in sorted_data)

def display_secret_message(url):
    """ Main function to fetch, parse, and display the secret message. """
    html = fetch_google_doc_html(url)
    grid_data, max_x, max_y = parse_table(html)

    if not grid_data:
        print("No valid grid data found. Check the document format.")
        return

    grid = create_grid(grid_data, max_x, max_y)
    print("\nSecret Message:")
    print_grid(grid)

# Run the function to display the secret message
display_secret_message(url)
