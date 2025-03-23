# Secret Message Extractor  

This Python script retrieves and deciphers a hidden message from a published Google Doc. It performs the following steps:  

1. **Fetches HTML Content** – Uses the `requests` library to retrieve the HTML of a publicly available Google Doc.  
2. **Parses Table Data** – Extracts Unicode characters and their (x, y) coordinates from an HTML table using BeautifulSoup.  
3. **Constructs a Grid** – Maps the extracted characters onto a 2D grid based on their coordinates.  
4. **Sorts and Reads the Message** – Arranges characters in the correct order and prints out the hidden message.  

To run the script, ensure you have `requests` and `BeautifulSoup` installed. Simply execute the script, and it will output the reconstructed message.  


![image](https://github.com/user-attachments/assets/3caafbbd-601e-46fa-9a16-b87fa55dbc56)
